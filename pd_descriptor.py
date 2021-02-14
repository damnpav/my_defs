import pandas as pd


def df_descriptor(df):
    """
    Function for short description of counts of unique values in each DF's columns
    :param df: Pandas DataFrame
    :return: Dictionary with columns of df as keys
    """
    descript_dict = dict.fromkeys(df.columns)
    for key in descript_dict.keys():
        descript_dict[key] = dict.fromkeys(pd.unique(df[key]))
        for key_1 in descript_dict[key].keys():
            descript_dict[key][key_1] = len(df[df[key] == key_1])
    return descript_dict
