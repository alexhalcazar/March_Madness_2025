import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from utils.data_loader import load_all_data_frames, get_basic_directory_path
from utils.data_cleaner import inspect_and_clean_data
from utils.data_validation import *
from utils.bias_analysis import *
from models.logistic_regression_model_alt import create_submission
from models.logreg_margOfVict_Rank import run_model
# import the data
dfs = load_all_data_frames()
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
M_file_path = os.path.join(get_basic_directory_path(), 'MNCAATourneyCompactResults.csv')
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
W_file_path = os.path.join(get_basic_directory_path(), 'WNCAATourneyCompactResults.csv')
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

file_path = os.path.join(get_basic_directory_path(), 'MRegularSeasonCompactResults.csv')
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


# team_stats, conf_stats

#### Run logistic regression model with features including team stats, margin of victory, ordinal rankings ####
#### and print accuracy score ####
run_model(dfs)
