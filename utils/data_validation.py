def validate_season(df, name):
  valid_seasons = (df['Season'] >= 1985) & (df['Season'] <= 2025)
  if not all(valid_seasons):
    print(f"Invalid season values found in {name}")
  else:
    print(f"All season values are valid in {name}")


def check_non_negative(col, df_name):
  print (f"All values in '{col.name}' of df '{df_name} are non-negative")
  return all(col >= 0)


def check_team_ids(col, df_name, team_ids):
  tourney_team_ids = set(col.unique())
  invalid_team_ids = tourney_team_ids - team_ids
  if invalid_team_ids:
    print(f"Invalid team IDs found in '{col.name}' of df '{df_name}': {invalid_team_ids}")
  else:
    print(f"All team IDs in '{col.name}' of df '{df_name}' are valid")
    