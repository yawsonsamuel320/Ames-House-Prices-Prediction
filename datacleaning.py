import pandas as pd

def print_hello(n=2):
    '''Prints hello'''
    return "hello"

def missing_percentage(df):
    '''missing_percentage(dataframe)

    Return the number and percentage of missing values

    Parameters
    ----------
    dataframe:

    Returns
    -------
    out: a Series
    A Series showing the levels of missing values


    '''
    NaN_count = df.isnull().sum().sort_values(ascending=False)
    NaN_count = NaN_count[NaN_count!=0]

    NaN_percent = (NaN_count / len(df)) * 100

    NaN_info = pd.concat([NaN_count, NaN_percent], axis=1, keys=["Total", "Percent"])

    return NaN_info
