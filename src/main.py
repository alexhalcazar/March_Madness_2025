import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

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



# Code covering representativeness, bias, and fairness of the data with accompanying graphs
def analyze_team_games(season_range=None):
    """
    Analyze the number of games played by each team and their win/loss records.
    
    Parameters:
    season_range (tuple): Optional tuple of (start_year, end_year) to filter seasons
    
    Returns:
    DataFrame with team game counts and win/loss statistics
    """
    # Define file paths
    basics_dir_path = os.path.join(os.getcwd(), 'data', 'section_1_basics')
    
    # Load team information
    teams_file = os.path.join(basics_dir_path, 'MTeams.csv')
    teams_df = pd.read_csv(teams_file)
    
    # Load regular season results
    reg_season_file = os.path.join(basics_dir_path, 'MRegularSeasonCompactResults.csv')
    reg_season_df = pd.read_csv(reg_season_file)
    
    # Load tournament results
    tourney_file = os.path.join(basics_dir_path, 'MNCAATourneyCompactResults.csv')
    tourney_df = pd.read_csv(tourney_file)
    
    # Filter by season range if provided
    if season_range:
        start_year, end_year = season_range
        reg_season_df = reg_season_df[(reg_season_df['Season'] >= start_year) & 
                                      (reg_season_df['Season'] <= end_year)]
        tourney_df = tourney_df[(tourney_df['Season'] >= start_year) & 
                                (tourney_df['Season'] <= end_year)]
    
    # Initialize dictionary to store team statistics
    team_stats = {}
    
    # Process all teams in the dataset
    for _, team in teams_df.iterrows():
        team_id = team['TeamID']
        team_name = team['TeamName']
        
        # Initialize stats for this team
        team_stats[team_id] = {
            'TeamName': team_name,
            'GamesPlayed': 0,
            'Wins': 0,
            'Losses': 0,
            'RegularSeasonGames': 0,
            'TournamentGames': 0,
            'HomeGames': 0,
            'AwayGames': 0,
            'NeutralGames': 0,
            'Seasons': set()
        }
    
    # Process regular season games
    for _, game in reg_season_df.iterrows():
        season = game['Season']
        w_team = game['WTeamID']
        l_team = game['LTeamID']
        w_loc = game['WLoc']
        
        # Update winning team stats
        if w_team in team_stats:
            team_stats[w_team]['GamesPlayed'] += 1
            team_stats[w_team]['Wins'] += 1
            team_stats[w_team]['RegularSeasonGames'] += 1
            team_stats[w_team]['Seasons'].add(season)
            
            if w_loc == 'H':
                team_stats[w_team]['HomeGames'] += 1
            elif w_loc == 'A':
                team_stats[w_team]['AwayGames'] += 1
            else:  # Neutral
                team_stats[w_team]['NeutralGames'] += 1
        
        # Update losing team stats
        if l_team in team_stats:
            team_stats[l_team]['GamesPlayed'] += 1
            team_stats[l_team]['Losses'] += 1
            team_stats[l_team]['RegularSeasonGames'] += 1
            team_stats[l_team]['Seasons'].add(season)
            
            if w_loc == 'A':  # If winner was away, loser was home
                team_stats[l_team]['HomeGames'] += 1
            elif w_loc == 'H':  # If winner was home, loser was away
                team_stats[l_team]['AwayGames'] += 1
            else:  # Neutral
                team_stats[l_team]['NeutralGames'] += 1
    
    # Process tournament games
    for _, game in tourney_df.iterrows():
        season = game['Season']
        w_team = game['WTeamID']
        l_team = game['LTeamID']
        
        # Update winning team stats
        if w_team in team_stats:
            team_stats[w_team]['GamesPlayed'] += 1
            team_stats[w_team]['Wins'] += 1
            team_stats[w_team]['TournamentGames'] += 1
            team_stats[w_team]['NeutralGames'] += 1  # Tournament games are neutral
            team_stats[w_team]['Seasons'].add(season)
        
        # Update losing team stats
        if l_team in team_stats:
            team_stats[l_team]['GamesPlayed'] += 1
            team_stats[l_team]['Losses'] += 1
            team_stats[l_team]['TournamentGames'] += 1
            team_stats[l_team]['NeutralGames'] += 1  # Tournament games are neutral
            team_stats[l_team]['Seasons'].add(season)
    
    # Convert to DataFrame
    stats_df = pd.DataFrame.from_dict(team_stats, orient='index')
    stats_df.reset_index(inplace=True)
    stats_df.rename(columns={'index': 'TeamID'}, inplace=True)
    
    # Calculate additional metrics
    stats_df['WinPercentage'] = (stats_df['Wins'] / stats_df['GamesPlayed'] * 100).round(2)
    stats_df['TournamentParticipationRate'] = (stats_df['TournamentGames'] / stats_df['GamesPlayed'] * 100).round(2)
    stats_df['NumSeasons'] = stats_df['Seasons'].apply(len)
    stats_df['AvgGamesPerSeason'] = (stats_df['GamesPlayed'] / stats_df['NumSeasons']).round(2)
    
    # Drop the set column which isn't needed for analysis
    stats_df.drop('Seasons', axis=1, inplace=True)
    
    return stats_df

def visualize_team_game_distribution(stats_df):
    """Create visualizations to analyze potential bias in game distribution"""
    
    # Set the aesthetic style
    sns.set(style="whitegrid")
    
    # Plot 1: Distribution of total games played
    plt.figure(figsize=(10, 6))
    sns.histplot(stats_df['GamesPlayed'], kde=True, bins=30)
    plt.title('Distribution of Total Games Played by Teams')
    plt.xlabel('Number of Games')
    plt.ylabel('Number of Teams')
    plt.show()
    
    # Plot 2: Games played vs. Win percentage
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='GamesPlayed', y='WinPercentage', data=stats_df, alpha=0.7)
    plt.title('Relationship Between Games Played and Win Percentage')
    plt.xlabel('Number of Games Played')
    plt.ylabel('Win Percentage')
    plt.show()
    
    # Plot 3: Home vs Away games comparison
    plt.figure(figsize=(12, 7))
    home_away_df = stats_df[stats_df['GamesPlayed'] > 100].copy()  # Filter teams with enough games
    home_away_df['HomeAdvantage'] = home_away_df['HomeGames'] / home_away_df['AwayGames']
    
    sns.scatterplot(x='HomeGames', y='AwayGames', 
                    size='WinPercentage', hue='WinPercentage',
                    data=home_away_df, alpha=0.7)
    
    # Add diagonal line representing equal home/away games
    max_val = max(home_away_df['HomeGames'].max(), home_away_df['AwayGames'].max())
    plt.plot([0, max_val], [0, max_val], 'r--', alpha=0.5)
    
    plt.title('Home vs Away Games (size and color indicate win percentage)')
    plt.xlabel('Home Games')
    plt.ylabel('Away Games')
    plt.show()
    
    # Plot 4: Tournament participation rate vs Win percentage
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='WinPercentage', y='TournamentParticipationRate', 
                   size='GamesPlayed', hue='NumSeasons', 
                   data=stats_df[stats_df['GamesPlayed'] > 50], alpha=0.7)
    plt.title('Tournament Participation vs Win Percentage')
    plt.xlabel('Win Percentage')
    plt.ylabel('Tournament Participation Rate (%)')
    plt.show()
    
    # Plot 5: Average games per season distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(stats_df['AvgGamesPerSeason'], kde=True, bins=20)
    plt.title('Distribution of Average Games per Season')
    plt.xlabel('Average Games per Season')
    plt.ylabel('Number of Teams')
    plt.show()
    
    # Plot 6: Top 20 teams by most games played
    plt.figure(figsize=(12, 8))
    top_teams = stats_df.nlargest(20, 'GamesPlayed')
    sns.barplot(x='TeamName', y='GamesPlayed', data=top_teams)
    plt.xticks(rotation=45, ha='right')
    plt.title('Top 20 Teams by Total Games Played')
    plt.tight_layout()
    plt.show()
    
    # Plot 7: Home vs Away win rate comparison (for teams with enough games)
    plt.figure(figsize=(10, 6))
    
    # Create a box plot showing the distribution of home/away games
    home_away_ratio = stats_df['HomeGames'] / (stats_df['HomeGames'] + stats_df['AwayGames'])
    sns.histplot(home_away_ratio[~home_away_ratio.isna()], kde=True, bins=20)
    plt.axvline(x=0.5, color='r', linestyle='--', alpha=0.7)
    plt.title('Distribution of Home Game Ratio')
    plt.xlabel('Home Games / (Home Games + Away Games)')
    plt.ylabel('Number of Teams')
    plt.show()

def conference_analysis(season_range=None):
    """
    Analyze potential bias in game distribution across conferences
    
    Parameters:
    season_range (tuple): Optional tuple of (start_year, end_year) to filter seasons
    
    Returns:
    DataFrame with conference statistics
    """
    # Define file paths
    basics_dir_path = os.path.join(os.getcwd(), 'data', 'section_1_basics')
    supplements_dir_path = os.path.join(os.getcwd(), 'data', 'section_5_supplements')
    
    # Load team information
    teams_file = os.path.join(basics_dir_path, 'MTeams.csv')
    teams_df = pd.read_csv(teams_file)
    
    # Load team conferences information
    team_conf_file = os.path.join(supplements_dir_path, 'MTeamConferences.csv')
    team_conf_df = pd.read_csv(team_conf_file)
    
    # Load conferences information
    conf_file = os.path.join(supplements_dir_path, 'Conferences.csv')
    conf_df = pd.read_csv(conf_file)
    
    # Load regular season results
    reg_season_file = os.path.join(basics_dir_path, 'MRegularSeasonCompactResults.csv')
    reg_season_df = pd.read_csv(reg_season_file)
    
    # Load tournament results
    tourney_file = os.path.join(basics_dir_path, 'MNCAATourneyCompactResults.csv')
    tourney_df = pd.read_csv(tourney_file)
    
    # Filter by season range if provided
    if season_range:
        start_year, end_year = season_range
        reg_season_df = reg_season_df[(reg_season_df['Season'] >= start_year) & 
                                      (reg_season_df['Season'] <= end_year)]
        tourney_df = tourney_df[(tourney_df['Season'] >= start_year) & 
                                (tourney_df['Season'] <= end_year)]
        team_conf_df = team_conf_df[(team_conf_df['Season'] >= start_year) & 
                                   (team_conf_df['Season'] <= end_year)]
    
    # Initialize dictionary to store conference statistics
    conf_stats = {}
    
    # Process each season
    for season in sorted(reg_season_df['Season'].unique()):
        # Get team conferences for this season
        season_confs = team_conf_df[team_conf_df['Season'] == season]
        
        # Process regular season games for this season
        season_games = reg_season_df[reg_season_df['Season'] == season]
        
        for _, game in season_games.iterrows():
            w_team = game['WTeamID']
            l_team = game['LTeamID']
            
            # Get conferences for both teams
            w_conf = season_confs[season_confs['TeamID'] == w_team]['ConfAbbrev'].values
            l_conf = season_confs[season_confs['TeamID'] == l_team]['ConfAbbrev'].values
            
            # Skip if conference information is missing
            if len(w_conf) == 0 or len(l_conf) == 0:
                continue
                
            w_conf = w_conf[0]
            l_conf = l_conf[0]
            
            # Initialize conference stats if needed
            for conf in [w_conf, l_conf]:
                if conf not in conf_stats:
                    conf_stats[conf] = {
                        'GamesPlayed': 0,
                        'Wins': 0,
                        'Losses': 0,
                        'IntraConferenceGames': 0,
                        'InterConferenceGames': 0,
                        'TournamentGames': 0,
                        'TournamentWins': 0,
                        'Seasons': set()
                    }
                conf_stats[conf]['Seasons'].add(season)
            
            # Update winning team's conference stats
            conf_stats[w_conf]['GamesPlayed'] += 1
            conf_stats[w_conf]['Wins'] += 1
            
            # Update losing team's conference stats
            conf_stats[l_conf]['GamesPlayed'] += 1
            conf_stats[l_conf]['Losses'] += 1
            
            # Check if intra or inter conference game
            if w_conf == l_conf:
                conf_stats[w_conf]['IntraConferenceGames'] += 1
            else:
                conf_stats[w_conf]['InterConferenceGames'] += 1
                conf_stats[l_conf]['InterConferenceGames'] += 1
    
        # Process tournament games for this season
        tourney_season_games = tourney_df[tourney_df['Season'] == season]
        
        for _, game in tourney_season_games.iterrows():
            w_team = game['WTeamID']
            l_team = game['LTeamID']
            
            # Get conferences for both teams
            w_conf = season_confs[season_confs['TeamID'] == w_team]['ConfAbbrev'].values
            l_conf = season_confs[season_confs['TeamID'] == l_team]['ConfAbbrev'].values
            
            # Skip if conference information is missing
            if len(w_conf) == 0 or len(l_conf) == 0:
                continue
                
            w_conf = w_conf[0]
            l_conf = l_conf[0]
            
            # Update tournament stats
            conf_stats[w_conf]['GamesPlayed'] += 1
            conf_stats[w_conf]['Wins'] += 1
            conf_stats[w_conf]['TournamentGames'] += 1
            conf_stats[w_conf]['TournamentWins'] += 1
            
            conf_stats[l_conf]['GamesPlayed'] += 1
            conf_stats[l_conf]['Losses'] += 1
            conf_stats[l_conf]['TournamentGames'] += 1
    
    # Convert to DataFrame
    stats_df = pd.DataFrame.from_dict(conf_stats, orient='index')
    stats_df.reset_index(inplace=True)
    stats_df.rename(columns={'index': 'ConfAbbrev'}, inplace=True)
    
    # Merge with conference names
    stats_df = pd.merge(stats_df, conf_df, on='ConfAbbrev', how='left')
    
    # Calculate additional metrics
    stats_df['WinPercentage'] = (stats_df['Wins'] / stats_df['GamesPlayed'] * 100).round(2)
    stats_df['TournamentWinPercentage'] = (stats_df['TournamentWins'] / stats_df['TournamentGames'] * 100).round(2)
    stats_df['IntraConfPercentage'] = (stats_df['IntraConferenceGames'] / stats_df['GamesPlayed'] * 100).round(2)
    stats_df['NumSeasons'] = stats_df['Seasons'].apply(len)
    stats_df['AvgGamesPerSeason'] = (stats_df['GamesPlayed'] / stats_df['NumSeasons']).round(2)
    
    # Drop the set column which isn't needed for analysis
    stats_df.drop('Seasons', axis=1, inplace=True)
    
    return stats_df

def visualize_conference_analysis(conf_stats_df):
    """Create visualizations to analyze potential bias across conferences"""
    
    # Set the aesthetic style
    sns.set(style="whitegrid")
    
    # Plot 1: Games played by conference
    plt.figure(figsize=(12, 8))
    top_confs = conf_stats_df.nlargest(20, 'GamesPlayed')
    sns.barplot(x='Description', y='GamesPlayed', data=top_confs)
    plt.xticks(rotation=45, ha='right')
    plt.title('Total Games Played by Top 20 Conferences')
    plt.tight_layout()
    plt.show()
    
    # Plot 2: Win percentage by conference
    plt.figure(figsize=(12, 8))
    # Filter to conferences with at least 100 games
    active_confs = conf_stats_df[conf_stats_df['GamesPlayed'] >= 100].copy()
    active_confs = active_confs.nlargest(20, 'WinPercentage')
    sns.barplot(x='Description', y='WinPercentage', data=active_confs)
    plt.xticks(rotation=45, ha='right')
    plt.title('Win Percentage by Conference (min 100 games)')
    plt.tight_layout()
    plt.show()
    
    # Plot 3: Tournament performance vs regular season performance
    plt.figure(figsize=(10, 6))
    # Filter to conferences with tournament games
    tourney_confs = conf_stats_df[conf_stats_df['TournamentGames'] > 0].copy()
    sns.scatterplot(x='WinPercentage', y='TournamentWinPercentage', 
                   size='TournamentGames', hue='NumSeasons',
                   data=tourney_confs, alpha=0.7)
    
    # Add diagonal line for reference
    plt.plot([30, 70], [30, 70], 'r--', alpha=0.5)
    
    plt.title('Tournament Performance vs Overall Performance')
    plt.xlabel('Overall Win Percentage')
    plt.ylabel('Tournament Win Percentage')
    plt.show()
    
    # Plot 4: Intra-conference game percentage
    plt.figure(figsize=(12, 8))
    intra_confs = conf_stats_df[conf_stats_df['GamesPlayed'] >= 100].copy()
    intra_confs = intra_confs.nlargest(20, 'IntraConfPercentage')
    sns.barplot(x='Description', y='IntraConfPercentage', data=intra_confs)
    plt.xticks(rotation=45, ha='right')
    plt.title('Percentage of Intra-Conference Games (min 100 games)')
    plt.tight_layout()
    plt.show()
    
    # Plot 5: Games played vs win percentage for all conferences
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='GamesPlayed', y='WinPercentage', 
                   size='NumSeasons', hue='TournamentGames',
                   data=conf_stats_df, alpha=0.7)
    plt.title('Games Played vs Win Percentage by Conference')
    plt.xlabel('Total Games Played')
    plt.ylabel('Win Percentage')
    plt.show()

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
