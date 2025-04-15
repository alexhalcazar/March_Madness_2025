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