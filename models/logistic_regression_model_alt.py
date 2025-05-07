import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import brier_score_loss
from sklearn.preprocessing import StandardScaler
from utils.data_loader import get_basic_directory_path
from sklearn.model_selection import train_test_split
from itertools import combinations

# Modeling Pipeline
# Load regular season results for a given gender ('M' or 'W')
def load_regular_season_results(gender):
    filename = f"{gender}RegularSeasonCompactResults.csv"
    return pd.read_csv(os.path.join(get_basic_directory_path(), filename))

# Load tournament seed data and extract numerical seed value
def load_seed_data(gender):
    filename = f"{gender}NCAATourneySeeds.csv"
    seeds_df = pd.read_csv(os.path.join(get_basic_directory_path(), filename))
    seeds_df['Seed'] = seeds_df['Seed'].str.extract('(\\d+)').astype(int)
    return seeds_df

# Aggregate average points and win rate statistics for each team
def build_team_stats(df):
    winning = df[['Season', 'WTeamID', 'WScore', 'LScore']].rename(
        columns={'WTeamID': 'TeamID', 'WScore': 'PointsFor', 'LScore': 'PointsAgainst'})
    winning['Win'] = 1

    losing = df[['Season', 'LTeamID', 'LScore', 'WScore']].rename(
        columns={'LTeamID': 'TeamID', 'LScore': 'PointsFor', 'WScore': 'PointsAgainst'})
    losing['Win'] = 0

    all_stats = pd.concat([winning, losing])
    team_stats = all_stats.groupby(['Season', 'TeamID']).agg(
        avg_points_for=('PointsFor', 'mean'),
        avg_points_against=('PointsAgainst', 'mean'),
        win_pct=('Win', 'mean')
    ).reset_index()
    return team_stats

# Train a logistic regression model for a given gender using regular season data
def train_model(gender):
    df = load_regular_season_results(gender)
    team_stats = build_team_stats(df)
    seeds_df = load_seed_data(gender)

    # Create labeled matchup data from real games
    matchups = df[['Season', 'WTeamID', 'LTeamID']].copy()
    matchups['Team1ID'] = matchups['WTeamID']
    matchups['Team2ID'] = matchups['LTeamID']
    matchups['Team1Won'] = 1

    # Merge in features for both teams
    for i in [1, 2]:
        matchups = matchups.merge(
            team_stats,
            how='left',
            left_on=['Season', f'Team{i}ID'],
            right_on=['Season', 'TeamID']
        ).merge(
            seeds_df,
            how='left',
            left_on=['Season', f'Team{i}ID'],
            right_on=['Season', 'TeamID']
        ).rename(columns={
            'avg_points_for': f'Team{i}_avg_points_for',
            'avg_points_against': f'Team{i}_avg_points_against',
            'win_pct': f'Team{i}_win_pct',
            'Seed': f'Team{i}_Seed'
        }).drop(columns=['TeamID_x', 'TeamID_y'])


    # Randomize order of teams to avoid label bias
    np.random.seed(42)
    swap_mask = np.random.rand(len(matchups)) < 0.5
    for col in ['avg_points_for', 'avg_points_against', 'win_pct', 'Seed']:
        matchups.loc[swap_mask, [f'Team1_{col}', f'Team2_{col}']] = matchups.loc[swap_mask, [f'Team2_{col}', f'Team1_{col}']].values
    matchups['Team1Won'] = (~swap_mask).astype(int)

    # Select features and train/test split
    feature_cols = [
        'Team1_avg_points_for', 'Team1_avg_points_against', 'Team1_win_pct', 'Team1_Seed',
        'Team2_avg_points_for', 'Team2_avg_points_against', 'Team2_win_pct', 'Team2_Seed']

    X = matchups[feature_cols].fillna(-1)
    y = matchups['Team1Won']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Print Brier score for model evaluation
    probs = model.predict_proba(X_test_scaled)[:, 1]
    brier = brier_score_loss(y_test, probs)
    print(f"{gender} Model Brier Score: {brier:.4f}")

    return model, scaler, team_stats, seeds_df

# Generate all valid matchups for a given season
def generate_matchups(team_df, season):
    team_ids = team_df['TeamID'].unique()
    pairs = [(a, b) for a, b in combinations(team_ids, 2)]
    return pd.DataFrame({
        'Season': season,
        'Team1ID': [min(a, b) for a, b in pairs],
        'Team2ID': [max(a, b) for a, b in pairs]
    })

# Create features and predict win probabilities for generated matchups
def create_features_and_predict(matchups, team_stats, seeds_df, model, scaler):
    for i in [1, 2]:
        matchups = matchups.merge(
            team_stats,
            how='left',
            left_on=['Season', f'Team{i}ID'],
            right_on=['Season', 'TeamID']
        ).merge(
            seeds_df,
            how='left',
            left_on=['Season', f'Team{i}ID'],
            right_on=['Season', 'TeamID']
        ).rename(columns={
            'avg_points_for': f'Team{i}_avg_points_for',
            'avg_points_against': f'Team{i}_avg_points_against',
            'win_pct': f'Team{i}_win_pct',
            'Seed': f'Team{i}_Seed'
        }).drop(columns=['TeamID_x', 'TeamID_y'])

    features = matchups[[
        'Team1_avg_points_for', 'Team1_avg_points_against', 'Team1_win_pct', 'Team1_Seed',
        'Team2_avg_points_for', 'Team2_avg_points_against', 'Team2_win_pct', 'Team2_Seed']].fillna(-1)

    features_scaled = scaler.transform(features)
    probs = model.predict_proba(features_scaled)[:, 1]

    matchups['ID'] = matchups.apply(lambda row: f"2025_{int(row.Team1ID)}_{int(row.Team2ID)}", axis=1)
    matchups['Pred'] = probs
    return matchups[['ID', 'Pred']]

# Main pipeline function to train both models and generate the submission file
def create_submission():
    # Train men's model and predict
    m_model, m_scaler, m_stats, m_seeds = train_model('M')
    m_teams = pd.read_csv(os.path.join(get_basic_directory_path(), "MTeams.csv"))
    m_matchups = generate_matchups(m_teams, 2025)
    m_preds = create_features_and_predict(m_matchups, m_stats, m_seeds, m_model, m_scaler)

    # Train women's model and predict
    w_model, w_scaler, w_stats, w_seeds = train_model('W')
    w_teams = pd.read_csv(os.path.join(get_basic_directory_path(), "WTeams.csv"))
    w_matchups = generate_matchups(w_teams, 2025)
    w_preds = create_features_and_predict(w_matchups, w_stats, w_seeds, w_model, w_scaler)

    # Save combined predictions to submission file
    submission = pd.concat([m_preds, w_preds])
    submission.to_csv("submission.csv", index=False)
    print("Submission file saved as submission.csv")