from stochastics.geometric_brownian_motion import geometric_brownian_motion as gbm
import pandas_market_calendars as mcal
import yfinance as yf
import pandas as pd


def price_path(ticker, model_start_date, model_end_date, drift, vol, exchange_name):
    """
    :param ticker: Ticker of the stock being modelled.
    :param model_start_date: Start date of the model in YYYY-MM-DD form.
    :param model_end_date: End date of the model in YYYY-MM-DD form.
    :param drift: Drift of the geometric Brownian motion.
    :param vol: Volatility of the geometric Brownian motion.
    :param exchange_name: Exchange that the security is traded on.
    :return: Price path as a pandas series.
    """

    exchange = mcal.get_calendar(exchange_name)
    market_open_times = exchange.schedule(start_date=model_start_date, end_date=model_end_date)

    asset = yf.Ticker(ticker)

    # Total trading days that the model covers.
    days = len(market_open_times)

    # Closest initial price to the model_start_date.
    initial_price = asset.history(start=model_start_date, end=model_end_date)['Open'][0]

    # Use geometric Brownian motion to model the asset and assign to a time series.
    path = gbm(n=days, x0=initial_price, t=days / 252, mu=drift, sigma=vol)
    series = pd.DataFrame(path, index=market_open_times['market_open'].index, columns=['close'])

    # Find dividends in the models date range.
    dividends_in_range = asset.dividends[model_start_date:model_end_date]

    # Implement dividends reductions.
    for date, dividend in dividends_in_range.iteritems():

        index_tmp = market_open_times['market_open'].index
        df_tmp = pd.DataFrame(data=0, index=index_tmp, columns=['close'])
        dividend_df = df_tmp[date:] + dividend

        series = series.subtract(dividend_df, fill_value=0)

    return series






