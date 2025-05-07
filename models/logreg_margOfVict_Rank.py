import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def run_model(dfs):
    # load the data 

    # load the regular season results
    games = dfs['MRegularSeasonCompactResults']

    # create data frames for team statistics 
    team_stats = build_team_stats(games)

    # generate matchups for the model
    matchups = generate_matchups(games, team_stats, dfs)

    # build feature matrix and labels 
    feature_cols = [
        'Team1_avg_points_for', 'Team1_avg_points_against', 'Team1_win_pct', 'Team1_avg_margin_of_victory',
        'Team2_avg_points_for', 'Team2_avg_points_against', 'Team2_win_pct', 'Team2_avg_margin_of_victory',
        'Team1Rank', 'Team2Rank', 'Team1RankDiff', 'Team1RankDiffAbs', 'Team1RankDiffPct', 'Team1RankDiffPctAbs'
    ]
    X = matchups[feature_cols]
    y = matchups['Team1Won']

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy with team stats, margin of victory and ordinal rankings: {accuracy:.3f}")



def build_team_stats(df):
    winning_stats = df[['Season', 'WTeamID', 'WScore', 'LScore']].rename(
    columns={'WTeamID': 'TeamID', 'WScore': 'PointsFor', 'LScore': 'PointsAgainst'}
    )
    winning_stats['Win'] = 1

    losing_stats = df[['Season', 'LTeamID', 'LScore', 'WScore']].rename(
        columns={'LTeamID': 'TeamID', 'LScore': 'PointsFor', 'WScore': 'PointsAgainst'}
    )
    losing_stats['Win'] = 0

    all_stats = pd.concat([winning_stats, losing_stats])

    all_stats['MarginOfVictory'] = all_stats['PointsFor'] - all_stats['PointsAgainst']

    # aggregate data to see averaage points for and against, and win percentage
    team_stats = all_stats.groupby(['Season', 'TeamID']).agg(
    avg_points_for=('PointsFor', 'mean'),
    avg_points_against=('PointsAgainst', 'mean'),
    win_pct=('Win', 'mean'),
    avg_margin_of_victory=('MarginOfVictory', 'mean')  # Add margin of victory
    ).reset_index()

    return team_stats

def generate_matchups(games, team_stats, dfs):
    # Create labeled matchup data from real games
    matchups = games[['Season', 'WTeamID', 'LTeamID']].copy()
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
        )
        matchups = matchups.rename(columns={
            'avg_points_for': f'Team{i}_avg_points_for',
            'avg_points_against': f'Team{i}_avg_points_against',
            'win_pct': f'Team{i}_win_pct',
            'avg_margin_of_victory': f'Team{i}_avg_margin_of_victory'  # Add margin of victory
        })
        matchups.drop(columns=['TeamID'], inplace=True)

    # randomly swap Team1 and Team2 
    np.random.seed(42)

    # Create a random boolean array: True means "swap"
    swap_mask = np.random.rand(len(matchups)) < 0.5

    # Swap team IDs by matching the mask
    matchups.loc[swap_mask, ['Team1ID', 'Team2ID']] = matchups.loc[swap_mask, ['Team2ID', 'Team1ID']].values
    for feature in ['avg_points_for', 'avg_points_against', 'win_pct']:
        team1_feature = f'Team1_{feature}'
        team2_feature = f'Team2_{feature}'
        matchups.loc[swap_mask, [team1_feature, team2_feature]] = matchups.loc[swap_mask, [team2_feature, team1_feature]].values

    # Set the target: 1 if original Team1 won, 0 if swapped
    matchups['Team1Won'] = (~swap_mask).astype(int)

    # add ordinal rankings to matchups
    matchups = merge_rankings(matchups, dfs)

    return matchups

def merge_rankings(matchups, dfs):
    # Load the rankings data
    rankings = dfs['MMasseyOrdinals']

    # keep only the relevant columns
    rankings = rankings[['Season', 'TeamID', 'OrdinalRank']]
    
    # keep the average ranking by season for each team
    rankings = rankings.groupby(['Season', 'TeamID']).agg(
        OrdinalRank=('OrdinalRank', 'mean')
    ).reset_index()

    # Add ordinal rankings for both Team1 and Team2
    for i in [1, 2]:
        matchups = matchups.merge(
            rankings, how='left',
            left_on=['Season', f'Team{i}ID'],
            right_on=['Season', 'TeamID']
        )
        matchups = matchups.drop(columns=['TeamID'])
        matchups = matchups.rename(columns={'OrdinalRank': f'Team{i}Rank'})

    # drop records with missing values in the rankings
    matchups = matchups.dropna(subset=['Team1Rank', 'Team2Rank'])

    # calculate rank difference
    matchups['Team1RankDiff'] = matchups['Team1Rank'] - matchups['Team2Rank']
    matchups['Team1RankDiffAbs'] = matchups['Team1RankDiff'].abs()
    matchups['Team1RankDiffPct'] = matchups['Team1RankDiff'] / matchups['Team2Rank']
    matchups['Team1RankDiffPctAbs'] = matchups['Team1RankDiffPct'].abs()

    return matchups