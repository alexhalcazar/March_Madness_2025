import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import seaborn as sns
from itertools import combinations
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import brier_score_loss
from utils.data_loader import load_all_data_frames
from utils.data_cleaner import inspect_and_clean_data
from utils.data_validation import *
from utils.bias_analysis import *

# import the data
dfs = load_all_data_frames()
basics_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_1_basics')
# handle missing data
cleaned_dfs = inspect_and_clean_data(dfs)

# Validate Data

# check that the Season column only contains years from 1985 to 2025
for key in ['MNCAATourneyCompactResults', 'MRegularSeasonCompactResults', 'MNCAATourneySeeds', 'MSeasons', 'WNCAATourneyCompactResults', 'WRegularSeasonCompactResults', 'WNCAATourneySeeds', 'WSeasons']:
  validate_season(dfs[key], key)

# check for negative numbers
for col in ['DayNum', 'WScore', 'LScore']:
   for df_name in ['MNCAATourneyCompactResults', 'MRegularSeasonCompactResults', 'WNCAATourneyCompactResults', 'WRegularSeasonCompactResults']:
     if col in dfs[df_name].columns:
       check_non_negative(dfs[df_name][col], df_name)

# check mens teams ids match with ids in the tourney_teams dataframe
team_ids = set(dfs['MTeams']['TeamID'].unique())

for df_name in ['MNCAATourneyCompactResults', 'MRegularSeasonCompactResults', 'MNCAATourneySeeds']:
  for col  in ['WTeamID', 'LTeamID', 'TeamID']:
    if col in dfs[df_name].columns:
      check_team_ids(dfs[df_name][col], df_name, team_ids)
  
# check womens teams ids are valid 
team_ids = set(dfs['WTeams']['TeamID'].unique())

for df_name in ['WNCAATourneyCompactResults', 'WRegularSeasonCompactResults', 'WNCAATourneySeeds']:
  for col  in ['WTeamID', 'LTeamID', 'TeamID']:
    if col in dfs[df_name].columns:
      check_team_ids(dfs[df_name][col], df_name, team_ids)

# validate regions
for df_name in ['MSeasons', 'WSeasons']:
  for col in ['RegionW', 'RegionX', 'RegionY', 'RegionZ']:
    if col in dfs[df_name].columns:
      print(f"Unique values in column '{col}' of df '{df_name}': {dfs[df_name][col].unique()}")

#Verifying Men's wins and losses data
M_file_path = os.path.join(basics_dir_path, 'MNCAATourneyCompactResults.csv')
df_m_tcr = pd.read_csv(M_file_path)
win_counts = df_m_tcr['WTeamID'].value_counts()
loss_counts = df_m_tcr['LTeamID'].value_counts()

team_ids = np.union1d(win_counts.index, loss_counts.index)

wins = win_counts.reindex(team_ids, fill_value=0)
losses = loss_counts.reindex(team_ids, fill_value=0)
total_wins = wins.sum()
total_losses = losses.sum()

fig, ax = plt.subplots(figsize=(20, 10))
x = np.arange(len(team_ids))

ax.bar(x - 0.25, wins, width=0.5, label="Wins", color='green', alpha=0.7)
ax.bar(x + 0.25, losses, width=0.5, label="Losses", color='red', alpha=0.7)

ax.set_xlabel("Team ID")
ax.set_ylabel("Total Number of Games")
ax.set_title("Wins and Losses in NCAA Tourney")
ax.legend()

plt.show()
print("TOTAL WINS: ", total_wins)
print("TOTAL LOSSES: ", total_losses)

#Classes are balanced with an equal number of wins as losses


#Verifying Women's wins and losses data
W_file_path = os.path.join(basics_dir_path, 'WNCAATourneyCompactResults.csv')
df_w_tcr = pd.read_csv(W_file_path)
win_counts = df_w_tcr['WTeamID'].value_counts()
loss_counts = df_w_tcr['LTeamID'].value_counts()

team_ids = np.union1d(win_counts.index, loss_counts.index)

wins = win_counts.reindex(team_ids, fill_value=0)
losses = loss_counts.reindex(team_ids, fill_value=0)
total_wins = wins.sum()
total_losses = losses.sum()

fig, ax = plt.subplots(figsize=(20, 10))
x = np.arange(len(team_ids))

ax.bar(x - 0.25, wins, width=0.5, label="Wins", color='green', alpha=0.7)
ax.bar(x + 0.25, losses, width=0.5, label="Losses", color='red', alpha=0.7)

ax.set_xlabel("Team ID")
ax.set_ylabel("Total Number of Games")
ax.set_title("Wins and Losses in NCAA Tourney")
ax.legend()

plt.show()
print("TOTAL WINS: ", total_wins)
print("TOTAL LOSSES: ", total_losses)

#Classes are balanced with an equal number of wins as losses

# Feature Distributions
# Plotting the distribution of winning and losing scores MRegularSeasonCompactResults.csv

file_path = os.path.join(basics_dir_path, 'MRegularSeasonCompactResults.csv')
df_m_reg = pd.read_csv(file_path)
                       
plt.figure(figsize=(10, 6))
plt.hist(df_m_reg["WScore"], bins=20, color='blue', alpha=0.7, label='Winning Score')
plt.hist(df_m_reg["LScore"], bins=20, color='orange', alpha=0.7, label='Losing Score')
plt.title("Distribution of Winning and Losing Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Here we are normalizing just one file for feedback

# Select columns to normalize
columns_to_normalize = ['WScore', 'LScore', 'DayNum', 'NumOT']

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Apply normalization
df_m_reg[columns_to_normalize] = scaler.fit_transform(df_m_reg[columns_to_normalize])

# Check the first few rows to verify the normalization
print(df_m_reg[['WScore', 'LScore', 'DayNum', 'NumOT']].head())


# Modeling Pipeline
# Load regular season results for a given gender ('M' or 'W')
def load_regular_season_results(gender):
    filename = f"{gender}RegularSeasonCompactResults.csv"
    return pd.read_csv(os.path.join(basics_dir_path, filename))

# Load tournament seed data and extract numerical seed value
def load_seed_data(gender):
    filename = f"{gender}NCAATourneySeeds.csv"
    seeds_df = pd.read_csv(os.path.join(basics_dir_path, filename))
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
    m_teams = pd.read_csv(os.path.join(basics_dir_path, "MTeams.csv"))
    m_matchups = generate_matchups(m_teams, 2025)
    m_preds = create_features_and_predict(m_matchups, m_stats, m_seeds, m_model, m_scaler)

    # Train women's model and predict
    w_model, w_scaler, w_stats, w_seeds = train_model('W')
    w_teams = pd.read_csv(os.path.join(basics_dir_path, "WTeams.csv"))
    w_matchups = generate_matchups(w_teams, 2025)
    w_preds = create_features_and_predict(w_matchups, w_stats, w_seeds, w_model, w_scaler)

    # Save combined predictions to submission file
    submission = pd.concat([m_preds, w_preds])
    submission.to_csv("submission.csv", index=False)
    print("Submission file saved as submission.csv")

# Entry Point
# Execute the submission pipeline when the script is run directly
if __name__ == "__main__":
    create_submission()

# actual print statement/function call for our defined functions above
# covered a variety of stats which can be modified to focus on certain seasons etc.
# Set season range if needed, e.g., (2010, 2023)
season_range = None  # Set to None to analyze all seasons

# Run team analysis
team_stats = analyze_team_games(season_range)
print("Team Statistics Summary:")
print(team_stats.describe())

# Print top 10 teams by games played
print("\nTop 10 Teams by Games Played:")
print(team_stats.nlargest(10, 'GamesPlayed')[['TeamName', 'GamesPlayed', 'Wins', 'Losses', 'WinPercentage']])

# Print top 10 teams by win percentage (minimum 100 games)
print("\nTop 10 Teams by Win Percentage (min 100 games):")
min_games = team_stats[team_stats['GamesPlayed'] >= 100]
print(min_games.nlargest(10, 'WinPercentage')[['TeamName', 'GamesPlayed', 'Wins', 'Losses', 'WinPercentage']])

# Visualize team analysis
visualize_team_game_distribution(team_stats)

# Run conference analysis
conf_stats = conference_analysis(season_range)
print("\nConference Statistics Summary:")
print(conf_stats.describe())

# Print top conferences by games played
print("\nTop 10 Conferences by Games Played:")
print(conf_stats.nlargest(10, 'GamesPlayed')[['Description', 'GamesPlayed', 'Wins', 'Losses', 'WinPercentage']])

# Visualize conference analysis
visualize_conference_analysis(conf_stats)

team_stats, conf_stats
