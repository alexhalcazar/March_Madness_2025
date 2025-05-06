import numpy as np


def inspect_and_clean_data(dfs):
    for name, df in dfs.items():
        print(name)
        print(df.info())
        # check for missing values
        print('Missing values per column:')
        print(df.isnull().sum())
        # Replace empty strings or spaces with NaN
        df.replace("", np.nan, inplace=True)
        # check duplicates
        print('Number of duplicates per column:')
        print(df.duplicated().sum())
    
        return dfs
