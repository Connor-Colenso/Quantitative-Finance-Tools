import yfinance as yf
import pandas as pd
import numpy as np


def implied_probability(ticker, date):

    data = yf.Ticker(ticker)

    if not (date in data.options):

        raise SystemExit('Invalid date for option chain.')

    options_chain = data.option_chain(date)

    puts = options_chain.puts
    calls = options_chain.calls

    puts_strikes = puts['strike']
    calls_strikes = calls['strike']

    puts_prices = options_chain.puts.lastPrice
    calls_prices = options_chain.calls.lastPrice

    print(pd.concat([puts_prices, puts_strikes]), axis=1)
