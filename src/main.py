import pandas as pd
import os

basics_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_1_basics')
team_box_scores_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_2_team_box_scores')
geography_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_3_geography')
public_rankings_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_4_public_rankings')
supplements_dir_path = os.path.join(os.path.dirname(__file__),'..','data','section_5_supplements')

# import the data
m_teams = pd.read_csv(os.path.join(basics_dir_path, 'Mteams.csv'))
# simple test to ensure we read properly
print(m_teams.head())