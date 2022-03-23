import random
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from tools.utility.funds import sp_500_stocks as sp500
import tools.utility.funds as funds
from tools.utility.correlation_matrix import correlation_matrix_generator
from tools.virtual_portfolio.portfolio import today, Portfolio
from tools.virtual_portfolio.trade import Trade
from tools.gbm_estimate_parameters import gbm_estimate_parameters
from tools.equities.price_path import price_path
import pandas as pd
from tools.utility.vol_smile import vol_smile


def main():

    pass


def estimate_stock_price_test():
    # Estimate stock price example:

    ticker = random.choice(sp500())

    model_start_date = '2015-01-01'
    model_end_date = '2016-01-01'

    input_data_start_date = '2013-01-01'
    input_data_end_date = '2015-01-01'

    exchange_name = 'NYSE'

    historical_data = yf.Ticker(ticker).history(start=input_data_start_date, end=input_data_end_date)['Close']

    drift, vol = gbm_estimate_parameters(x=list(historical_data), t=len(historical_data) / 252)

    series = price_path(ticker, model_start_date, model_end_date, drift, vol, exchange_name)
    plt.plot(series, color='red', label='Price projection')

    plt.plot(yf.Ticker(ticker).history(start=model_start_date, end=model_end_date)['Close'], color='green', label='Historical data')
    plt.plot(historical_data, color='blue', label='Sample data')

    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.title(f'{ticker} Price Projection {model_start_date} to {model_end_date}')
    plt.subplots_adjust(bottom=0.2)
    plt.savefig(f'image_dump/estimate_stock_price_test - {ticker}.png', dpi=1200)
    plt.show()


def correlation_matrix_test():
    assets = funds.sp_500_stocks()[110:115]

    correlation_matrix_generator(assets, period='1y', interval='1d', visual=True,
                                 img_name='TEST1')


def portfolio_test():
    initial_cash = 100000
    assets = []

    csv = pd.read_csv('Alpha Fund - Sheet1.csv')

    for index, row in csv.iterrows():

        date_sold = row['Date Sold']

        if np.isnan(date_sold):
            date_sold = today()

        assets.append(Trade(ticker=row['Ticker'],
                            quantity=row['Quantity'],
                            date_purchased=row['Purchase Date'],
                            date_sold=date_sold,
                            asset_type=row['Asset Type'],
                            leverage=row['Leverage'],
                            short=row['Short']))

    alpha_fund = Portfolio(initial_cash=initial_cash, assets=assets)

    alpha_fund.pct_return_graph(benchmark='^FTSE', name='Alpha Fund Portfolio')
    alpha_fund.pie_chart(name='Alpha Fund Portfolio')
    alpha_fund.abs_return_graph(name='Alpha Fund Portfolio')
    alpha_fund.correlation_matrix(name='Alpha Fund Portfolio')


def vol_smile_test():

    vol_smile(ticker='AAPL')


if __name__ == '__main__':

    # portfolio_test()
    # correlation_matrix_test()
    estimate_stock_price_test()
    # vol_smile_test()
