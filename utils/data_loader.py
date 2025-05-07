import os
import pandas as pd

def load_all_data_frames():
    # Get the absolute path of the current script's directory (src)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct paths to the data directories (relative to the root project folder)
    data_dir = os.path.join(current_dir, '..', 'data')
    basics_dir_path = os.path.join(data_dir, 'section_1_basics')
    team_box_scores_dir_path = os.path.join(data_dir, 'section_2_team_box_scores')
    geography_dir_path = os.path.join(data_dir, 'section_3_geography')
    public_rankings_dir_path = os.path.join(data_dir, 'section_4_public_rankings')
    supplements_dir_path = os.path.join(data_dir, 'section_5_supplements')

    dfs = {}
    for path in [basics_dir_path, team_box_scores_dir_path, geography_dir_path, public_rankings_dir_path, supplements_dir_path]:
        for filename in os.listdir(path):
            if filename.endswith(".csv"):
                filepath = os.path.join(path, filename)
                df_name = filename[:-4]  # Remove the .csv extension
                dfs[df_name] = pd.read_csv(filepath)
    dfs.keys()

    return dfs

def get_basic_directory_path():
     return os.path.join(os.path.dirname(__file__),'..','data','section_1_basics')
     