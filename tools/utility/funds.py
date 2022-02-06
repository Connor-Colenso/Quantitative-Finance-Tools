import pandas as pd


def sp_500_stocks():
    """
    :return: Returns a list of all the companies in the S&P 500 index.
    """
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    return tuple(table[0]['Symbol'])


def ftse_100_stocks():
    """
    :return: Returns a list of all the companies in the FTSE 100 index.
    """

    table = pd.read_html('https://en.wikipedia.org/wiki/FTSE_100_Index')

    return tuple(table[0]['EPIC'])
