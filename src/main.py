import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# import the data
basics_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_1_basics')
team_box_scores_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_2_team_box_scores')
geography_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_3_geography')
public_rankings_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_4_public_rankings')
supplements_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_5_supplements')

# handle missing data
# Pass in a folder and iterate through each file in the folder
def data_completeness(directory_path):
    directory = os.listdir(directory_path)
    for file in directory:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            df.info()
            # Replace empty strings or spaces with NaN
            df.replace("", np.nan, inplace=True)
            # check duplicates
            num_duplicates = df.duplicated().sum()
            # check for missing values
            missing_val_count_by_column = df.isnull().sum()
            if missing_val_count_by_column.any():
                print(f'Missing values for ${file} is: ${missing_val_count_by_column[missing_val_count_by_column > 0]}')
            if num_duplicates.any():
                print(f'We have duplicate values for ${file} is: ${num_duplicates}')

data_completeness(basics_dir_path)
data_completeness(team_box_scores_dir_path)
data_completeness(geography_dir_path)
data_completeness(public_rankings_dir_path)
data_completeness(supplements_dir_path)


#######################################################################################################################################
# Validate Data
# Convert files to dataframes
dfs = {}
for filename in os.listdir(basics_dir_path):
  if filename.endswith(".csv"):
    filepath = os.path.join(basics_dir_path, filename)
    df_name = filename[:-4]  # Remove the .csv extension
    dfs[df_name] = pd.read_csv(filepath)
dfs.keys()

# check that the Season column only contains years from 1985 to 2025
def validate_season(df, name):
  valid_seasons = (df['Season'] >= 1985) & (df['Season'] <= 2025)
  if not all(valid_seasons):
    print(f"Invalid season values found in {name}")
  else:
    print(f"All season values are valid in {name}")
  
for key in ['MNCAATourneyCompactResults', 'MRegularSeasonCompactResults', 'MNCAATourneySeeds', 'MSeasons', 'WNCAATourneyCompactResults', 'WRegularSeasonCompactResults', 'WNCAATourneySeeds', 'WSeasons']:
  validate_season(dfs[key], key)

# check for negative numbers

def check_non_negative(col, df_name):
  print (f"All values in '{col.name}' of df '{df_name} are non-negative")
  return all(col >= 0)

for col in ['DayNum', 'WScore', 'LScore']:
   for df_name in ['MNCAATourneyCompactResults', 'MRegularSeasonCompactResults', 'WNCAATourneyCompactResults', 'WRegularSeasonCompactResults']:
     if col in dfs[df_name].columns:
       check_non_negative(dfs[df_name][col], df_name)

# check mens teams ids match with ids in the tourney_teams dataframe
team_ids = set(dfs['MTeams']['TeamID'].unique())

def check_team_ids(col, df_name):
  tourney_team_ids = set(col.unique())
  invalid_team_ids = tourney_team_ids - team_ids
  if invalid_team_ids:
    print(f"Invalid team IDs found in '{col.name}' of df '{df_name}': {invalid_team_ids}")
  else:
    print(f"All team IDs in '{col.name}' of df '{df_name}' are valid")

for df_name in ['MNCAATourneyCompactResults', 'MRegularSeasonCompactResults', 'MNCAATourneySeeds']:
  for col  in ['WTeamID', 'LTeamID', 'TeamID']:
    if col in dfs[df_name].columns:
      check_team_ids(dfs[df_name][col], df_name)
  
# check womens teams ids are valid 
team_ids = set(dfs['WTeams']['TeamID'].unique())

for df_name in ['WNCAATourneyCompactResults', 'WRegularSeasonCompactResults', 'WNCAATourneySeeds']:
  for col  in ['WTeamID', 'LTeamID', 'TeamID']:
    if col in dfs[df_name].columns:
      check_team_ids(dfs[df_name][col], df_name)

# validate regions
for df_name in ['MSeasons', 'WSeasons']:
  for col in ['RegionW', 'RegionX', 'RegionY', 'RegionZ']:
    if col in dfs[df_name].columns:
      print(f"Unique values in column '{col}' of df '{df_name}': {dfs[df_name][col].unique()}")
#######################################################################################################################################


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