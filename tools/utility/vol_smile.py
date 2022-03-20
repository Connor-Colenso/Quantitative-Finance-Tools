import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.parser import parse

# def date_to_expiry_converter(date):
#
#     start_date = datetime.today()
#     end_date = datetime.strptime(date,'%Y-%m-%d')
#
#     diff = end_date - start_date
#
#     return diff.days / 365


def vol_smile(expiry=None, *, ticker):
    asset = yf.Ticker(ticker)

    if expiry is None:
        expiry = asset.options[0]

    calls = asset.option_chain(expiry).calls
    puts = asset.option_chain(expiry).puts

    plt.plot(calls.strike, calls.impliedVolatility, lw=1, color='red', label='Calls')
    plt.plot(puts.strike, puts.impliedVolatility, lw=1, color='blue', label='Puts')

    plt.legend()
    plt.title(f'Volatility smile for options expiring on {expiry} as of {datetime.today().strftime("%Y-%m-%d")}')
    plt.xlabel('Strike Price')
    plt.ylabel('Implied Volatility')

    # X = [date_to_expiry_converter(date) for date in asset.options]

    plt.show()
