# %% [markdown]
# 
# # Logistic Regression
# ## 1. Import data to dataframes

# %%
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# import the data
current_dir = os.getcwd()
basics_dir_path = os.path.join(current_dir, '..', 'data', 'section_1_basics')
team_box_scores_dir_path = os.path.join(current_dir, '..', 'data', 'section_2_team_box_scores')
geography_dir_path = os.path.join(current_dir, '..', 'data','section_3_geography')
public_rankings_dir_path = os.path.join(current_dir, '..','data', 'section_4_public_rankings')
supplements_dir_path = os.path.join(current_dir, '..', 'data', 'section_5_supplements')

# %%
dfs = {}
for path in [basics_dir_path, team_box_scores_dir_path, geography_dir_path, public_rankings_dir_path, supplements_dir_path]:
  for filename in os.listdir(path):
    if filename.endswith(".csv"):
      filepath = os.path.join(path, filename)
      df_name = filename[:-4]  # Remove the .csv extension
      dfs[df_name] = pd.read_csv(filepath)
dfs.keys()

# %% [markdown]
# ## 2. For this model we are going to use the data from `MRegularSeasonCompactResults.csv`

# %%
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

# %%

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Set Accuracy: {accuracy:.3f}")


