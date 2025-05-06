# %% [markdown]
# 
# # Logistic Regression
# ## 1. Import data to dataframes

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from utils.data_loader import load_all_data_frames
# %% [markdown]
# ## 2. For this model we are going to use the data from `MRegularSeasonCompactResults.csv`

# %%
dfs = load_all_data_frames()
games = dfs['MRegularSeasonCompactResults']
games

# %% [markdown]
# ## 3. Create a dataframe containing the regular game statistics for each match of each season.

# %%
winning_stats = games[['Season', 'WTeamID', 'WScore', 'LScore']].rename(
    columns={'WTeamID': 'TeamID', 'WScore': 'PointsFor', 'LScore': 'PointsAgainst'}
)
winning_stats['Win'] = 1

losing_stats = games[['Season', 'LTeamID', 'LScore', 'WScore']].rename(
    columns={'LTeamID': 'TeamID', 'LScore': 'PointsFor', 'WScore': 'PointsAgainst'}
)
losing_stats['Win'] = 0

all_stats = pd.concat([winning_stats, losing_stats])
all_stats

# %% [markdown]
# #### Aggregate the data see the average points scored, average points scored against, and win percentage

# %%
team_stats = all_stats.groupby(['Season', 'TeamID']).agg(
    avg_points_for=('PointsFor', 'mean'),
    avg_points_against=('PointsAgainst', 'mean'),
    win_pct=('Win', 'mean')
).reset_index()
team_stats

# %% [markdown]
# ## 4. Create dataframe containing the matchups and merge in data from the statistics dataframe

# %%
matchups = games[['Season', 'WTeamID', 'LTeamID']].copy()
matchups['Team1ID'] = matchups['WTeamID']
matchups['Team2ID'] = matchups['LTeamID']
matchups['Team1Won'] = 1  # Because WTeamID is the winner in your dataset
matchups

# %% [markdown]
# #### Merge in team stats for Team1

# %%
matchups = matchups.merge(
    team_stats, how='left',
    left_on=['Season', 'Team1ID'],
    right_on=['Season', 'TeamID']
)
matchups = matchups.rename(columns={
    'avg_points_for': 'Team1_avg_points_for',
    'avg_points_against': 'Team1_avg_points_against',
    'win_pct': 'Team1_win_pct'
})
matchups = matchups.drop(columns=['TeamID'])

# %% [markdown]
# #### Merge in stats for Team2

# %%
# merge stats for Team2
matchups = matchups.merge(
    team_stats, how='left',
    left_on=['Season', 'Team2ID'],
    right_on=['Season', 'TeamID']
)
matchups = matchups.rename(columns={
    'avg_points_for': 'Team2_avg_points_for',
    'avg_points_against': 'Team2_avg_points_against',
    'win_pct': 'Team2_win_pct'
})
matchups = matchups.drop(columns=['TeamID'])

# %% [markdown]
# #### Randomly swap Team1 and Team2 to create 2 classes for the 'Team1' column

# %%
np.random.seed(42)  # for reproducibility

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

# %% [markdown]
# ## 5. Build feature matrix and labels

# %%
feature_cols = [
    'Team1_avg_points_for', 'Team1_avg_points_against', 'Team1_win_pct',
    'Team2_avg_points_for', 'Team2_avg_points_against', 'Team2_win_pct'
]

X = matchups[feature_cols]
y = matchups['Team1Won']

# %% [markdown]
# #### Train/test split

# %%
# Step 5: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %% [markdown]
# ## 6. Scale features

# %%
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# %% [markdown]
# ## 7. Train the model

# %%
# Step 7: Train the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# %% [markdown]
# ## 8. Evaluate
# This model gives an accuracy score of 74.2%. 

# %%

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Set Accuracy: {accuracy:.3f}")

# %% [markdown]
# ## 9. Add margin of victory to team stats to improve the model
# The margin of victory is the difference between the points scored by the winning team and the points scored by the losing team.
# This is a common feature used in sports analytics to predict the outcome of games.
# The margin of victory is a good predictor of the outcome of a game because it takes into account the strength of both teams.
# A team that wins by a large margin is likely to be stronger than a team that wins by a small margin.
# 
# To do this, we will add the margin of victory to the team stats dataframe and then re-run the model.
# %% 
# Combine winning and losing stats into a single dataframe
winning_stats = games[['Season', 'WTeamID', 'WScore', 'LScore']].rename(
    columns={'WTeamID': 'TeamID', 'WScore': 'PointsFor', 'LScore': 'PointsAgainst'}
)
winning_stats['Win'] = 1

losing_stats = games[['Season', 'LTeamID', 'LScore', 'WScore']].rename(
    columns={'LTeamID': 'TeamID', 'LScore': 'PointsFor', 'WScore': 'PointsAgainst'}
)
losing_stats['Win'] = 0

all_stats = pd.concat([winning_stats, losing_stats])

# Compute margin of victory per game
all_stats['MarginOfVictory'] = all_stats['PointsFor'] - all_stats['PointsAgainst']  

# Aggregate by season and team
team_stats = all_stats.groupby(['Season', 'TeamID']).agg(
    avg_points_for=('PointsFor', 'mean'),
    avg_points_against=('PointsAgainst', 'mean'),
    win_pct=('Win', 'mean'),
    avg_margin_of_victory=('MarginOfVictory', 'mean')  # Add margin of victory
).reset_index()

# %% [markdown]
# #### Build matchups, merge in the new stats for both teams
# %%
# Merge in stats for Team1
matchups = matchups.merge(
    team_stats, how='left',
    left_on=['Season', 'Team1ID'],
    right_on=['Season', 'TeamID']
)
matchups = matchups.rename(columns={
    'avg_points_for': 'Team1_avg_points_for',
    'avg_points_against': 'Team1_avg_points_against',
    'win_pct': 'Team1_win_pct',
    'avg_margin_of_victory': 'Team1_avg_margin_of_victory'  # Add margin of victory
})
matchups = matchups.drop(columns=['TeamID'])

# Merge in stats for Team2
matchups = matchups.merge(
    team_stats, how='left',
    left_on=['Season', 'Team2ID'],
    right_on=['Season', 'TeamID']
)
matchups = matchups.rename(columns={
    'avg_points_for': 'Team2_avg_points_for',
    'avg_points_against': 'Team2_avg_points_against',
    'win_pct': 'Team2_win_pct',
    'avg_margin_of_victory': 'Team2_avg_margin_of_victory'  # Add margin of victory
})
matchups = matchups.drop(columns=['TeamID'])

# %%
# Update feature columns to include margin of victory
feature_cols = [
    'Team1_avg_points_for', 'Team1_avg_points_against', 'Team1_win_pct', 'Team1_avg_margin_of_victory',
    'Team2_avg_points_for', 'Team2_avg_points_against', 'Team2_win_pct', 'Team2_avg_margin_of_victory'
]

# %%
# Build feature matrix and labels
X = matchups[feature_cols]
y = matchups['Team1Won']
# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Train the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
# Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Set Accuracy with Margin of Victory: {accuracy:.3f}")
# %% [markdown]
# The model with the margin of victory feature has an accuracy of 74.2%.
# This is the same performance for the model without the margin of victory feature.
#
# The margin of victory feature does not improve the model's performance.

# %% [markdown]
# ## 10. Add Ranking Features
# We are going to use data from this file `MMasseyOrdinals.csv` to add ranking features to the model.
# This file contains the rankings of each team for each season. We will use the rankings to create new features for the model.
# The features we will create are:
# - Team1Rank: The ranking of Team1 for the season
# - Team2Rank: The ranking of Team2 for the season
# - Team1RankDiff: The difference between the rankings of Team1 and Team2
# - Team1RankDiffAbs: The absolute difference between the rankings of Team1 and Team2
# - Team1RankDiffPct: The percentage difference between the rankings of Team1 and Team2
# - Team1RankDiffPctAbs: The absolute percentage difference between the rankings of Team1 and Team2

# %%
rankings = dfs['MMasseyOrdinals']
# %%
rankings = rankings[['Season', 'TeamID', 'OrdinalRank']]
# %% 
# keep the average ranking by season for each team
rankings = rankings.groupby(['Season', 'TeamID']).agg(
    OrdinalRank=('OrdinalRank', 'mean')
).reset_index()


# %% [markdown]
# #### Merge in rankings for Team1

# %%
matchups = matchups.merge(
    rankings, how='left',
    left_on=['Season', 'Team1ID'],
    right_on=['Season', 'TeamID']
)

#%% 
#%%
# drop TeamID from the matchups dataframe
matchups = matchups.drop(columns=['TeamID'])

#%% 
# rename the column of the matchups dataframe for Team1Rank
matchups = matchups.rename(columns={'OrdinalRank': 'Team1Rank'})

# %% [markdown]
# #### Merge in rankings for Team2
# %%
matchups = matchups.merge(
    rankings, how='left',
    left_on=['Season', 'Team2ID'],
    right_on=['Season', 'TeamID']
)

#%%
# drop TeamID from the matchups dataframe and rename column for Team2Rank
matchups = matchups.drop(columns=['TeamID'])
matchups = matchups.rename(columns={'OrdinalRank': 'Team2Rank'})

# %% [markdown]
# #### Check for missing values in the rankings
# %%
matchups.isna().sum()
# %%
# drop records with missing values in the rankings
matchups = matchups.dropna(subset=['Team1Rank', 'Team2Rank'])

# %%
# Calculate ranking differences
matchups['Team1RankDiff'] = matchups['Team1Rank'] - matchups['Team2Rank']
matchups['Team1RankDiffAbs'] = matchups['Team1RankDiff'].abs()
matchups['Team1RankDiffPct'] = matchups['Team1RankDiff'] / matchups['Team2Rank']
matchups['Team1RankDiffPctAbs'] = matchups['Team1RankDiffPct'].abs()
matchups

# %%
# Update feature columns to include ranking features
feature_cols = [
    'Team1_avg_points_for', 'Team1_avg_points_against', 'Team1_win_pct', 'Team1_avg_margin_of_victory',
    'Team2_avg_points_for', 'Team2_avg_points_against', 'Team2_win_pct', 'Team2_avg_margin_of_victory',
    'Team1Rank', 'Team2Rank', 'Team1RankDiff', 'Team1RankDiffAbs', 'Team1RankDiffPct', 'Team1RankDiffPctAbs'
]
# %%
# Build feature matrix and labels
X = matchups[feature_cols]
y = matchups['Team1Won']


# %%
# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%% 
# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#%%
# Train the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
#%%
# Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Set Accuracy with rankings: {accuracy:.3f}")

# %% [markdown]
# ## 11. Conclusion
# The model with the margin of victory and rankings features has an accuracy of 75.8%.
# This is an improvement over the model without these features, which had an accuracy of 74.2%.
#
# The model with the margin of victory and rankings features is a better predictor of the outcome of a game than the model without these features.  

