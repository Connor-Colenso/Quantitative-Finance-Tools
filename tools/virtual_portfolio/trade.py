from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np


class Trade:
    """
    Individual trade that can be placed into the Portfolio object. Data is sourced using Yahoo Finance.
    """

    def __init__(self, *, ticker, quantity, date_purchased, asset_type, date_sold=datetime.today(), leverage=1,
                 short=False, market='NYSE'):

        self.ticker = ticker
        self.quantity = quantity
        self.asset_type = asset_type
        self.date_sold = date_sold
        self.leverage = leverage
        self.short = short

        # Check that the date is in the correct format and convert to datetime if it's a string.
        if isinstance(date_purchased, str):
            self.date_purchased = datetime.strptime(date_purchased, '%Y-%m-%d')
        elif isinstance(date_purchased, datetime):
            self.date_purchased = date_purchased.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            raise Exception('Invalid type for date_purchased.')

        if isinstance(date_sold, str):
            self.date_sold = datetime.strptime(date_sold, '%Y-%m-%d')
        elif isinstance(date_sold, datetime):
            self.date_sold = date_sold.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            raise Exception('Invalid type for date_sold.')

        asset = yf.Ticker(ticker)
        price_history = asset.history(self.ticker, start=self.date_purchased, end=self.date_sold)['Close']

        if len(price_history) == 0:
            raise Exception('Price history is empty.')

        if price_history.index[0] != self.date_purchased:
            raise Exception(f'Invalid date range for {self.ticker} asset. Oldest date is {price_history.index[0]}.')

        self.purchase_price = price_history[0]

        # Fill in the date gaps for dates when market is closed with NaN and then backfill those gaps with future
        # values. This is essential for ensuring that the graphing of the portfolio can be done correctly as some
        # assets are traded 24/7 i.e. crypto.
        price_history = price_history.resample('1D').mean().ffill()
        percentage_return = (1 + self.leverage * np.sign((not self.short) - 0.5) * (
                price_history - self.purchase_price) / self.purchase_price)

        self.valuation_history = self.quantity * self.purchase_price * percentage_return
        self.percentage_return = percentage_return

        # If this is an equity we must define what market it is traded on. Usually NYSE.
        if asset_type == 'equity':
            self.market = market

            # Equities are not traded on weekends.
            if self.date_sold.weekday() > 5:
                raise Exception('Invalid purchase date. Equities markets are closed on weekends.')

        # Sanity checks
        if self.date_purchased > self.date_sold:
            raise Exception('Date sold is before date purchased.')

        if quantity <= 0:
            raise Exception('Quantity purchased is negative or 0.')

        if leverage <= 0:
            raise Exception('Leverage is negative or 0.')

        if not isinstance(short, bool):
            raise Exception('Short should be a boolean value.')

    def __repr__(self):
        return self.ticker

    def value(self):
        """
        :return: Current value of this asset of liquidated.
        """
        return self.valuation_history[0]

    def graph(self):
        """
        :return: None
        """
        price_history = self.quantity * self.valuation_history
        plt.plot(price_history, lw=1, color='black')
        plt.xticks(rotation=45)
        plt.subplots_adjust(bottom=0.21)
        plt.subplots_adjust(left=0.15)
        plt.xlabel('Date')
        plt.ylabel('Value (USD $)')
        plt.title(self.ticker)
        plt.show()
