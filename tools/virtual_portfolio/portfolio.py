from datetime import datetime, timedelta
from tools.utility.correlation_matrix import correlation_matrix_generator
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


def today():
    """
    :return: Datetime object of todays date. All other attributes are set to zero out.
    """
    return datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)


class Portfolio:
    """
    Portfolio object, can hold an arbitrary number of assets or pure cash.
    """

    def __init__(self, *, initial_cash, assets):
        self.asset_list = assets
        self.initial_cash = initial_cash

    def cash_history(self):
        """
        :return: Cash in the portfolio over time.
        """

        purchase_list = [asset.date_purchased for asset in self.asset_list]
        oldest_purchase = min(purchase_list)

        cash_dates = pd.date_range(oldest_purchase, datetime.today() - timedelta(days=1), freq='D')
        df = pd.DataFrame([self.initial_cash] * len(cash_dates)).set_index(cash_dates)
        df.columns = ['initial_cash']

        cash_list = []

        for asset in self.asset_list:

            if asset.date_sold == today():
                date_sold = today() - timedelta(days=1)
            else:
                date_sold = asset.date_sold

            cash_dates = pd.date_range(asset.date_purchased, date_sold, freq='D')
            tmp_df = pd.DataFrame([-asset.purchase_price * asset.quantity] * len(cash_dates)).set_index(cash_dates)
            tmp_df.columns = [asset.ticker]

            cash_list.append(tmp_df)

        cash_history = pd.concat([df] + cash_list, axis=1).fillna(0)
        cash_history['sum'] = cash_history.sum(axis=1)

        return cash_history['sum']

    def cash(self):
        """
        :return: Current cash held in the portfolio.
        """
        return self.cash_history()[-1]

    def add_trade(self, asset):
        """
        :param asset: Asset in the form of a Trade object.
        :return: None
        """
        self.asset_list.append(asset)

    def value(self):
        """
        :return: Value of the portfolio at the present time.
        """

        return self.portfolio_valuation()['sum'][-1]

    def portfolio_valuation(self):
        """
        :return: DataFrame containing the padded portfolios value over time. If a date has no data then it will check
        backwards in time until itn finds valid data to substitute.
        """

        df = pd.concat([asset.valuation_history for asset in self.asset_list] + [self.cash_history()], axis=1)
        df.columns = [asset.ticker for asset in self.asset_list] + ['CASH']
        df['sum'] = df.sum(axis=1)

        row_to_drop = 0
        for i in range(len(df), 0, -1):
            if df[i - 1:i].isnull().values.any():
                row_to_drop += 1
            else:
                break

        return df[0:len(df) - row_to_drop].fillna(0)

    def abs_return_graph(self, *, name):

        plt.plot(self.portfolio_valuation().index, self.portfolio_valuation()['sum'], lw=1, color='black')
        plt.xticks(rotation=45)
        plt.subplots_adjust(bottom=0.21)
        plt.subplots_adjust(left=0.15)
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value (USD $)')
        plt.title(name)
        plt.savefig(f'image_dump/{name} - portfolio value.png', dpi=100)
        plt.show()

    def pct_return_graph(self, *, benchmark, name):
        """
        :param benchmark: Benchmark asset to compare against. Usually the FTSE100 or S&P500.
        :param name: Name of the graph and image name.
        :return: None
        """

        portfolio_pct_return = self.portfolio_valuation()['sum'].pct_change()

        purchase_list = [asset.date_purchased for asset in self.asset_list]
        oldest_purchase = min(purchase_list)

        asset = yf.Ticker(benchmark).history(start=oldest_purchase, end=today())['Close']

        benchmark_pct_return = asset.pct_change()

        plt.plot(self.portfolio_valuation().index, portfolio_pct_return, lw=1, color='black',
                 label='Portfolio Returns')

        plt.plot(benchmark_pct_return.index, benchmark_pct_return, lw=1, color='green',
                 label=f'Benchmark Returns ({benchmark})')

        plt.legend()
        plt.xticks(rotation=45)
        plt.subplots_adjust(bottom=0.21)
        plt.subplots_adjust(left=0.15)
        plt.xlabel('Date')
        plt.ylabel('Percentage Return (%)')
        plt.title(name)
        plt.savefig(f'image_dump/{name} - pct return.png', dpi=100)
        plt.show()

    def pie_chart(self, *, name):
        """
        :param name: Name of the chart and image name.
        :return: None
        """

        df = self.portfolio_valuation()

        labels = []
        values = []

        for column in df:

            if column != 'sum':

                labels.append(column)
                values.append(df[column][-1])

        plt.pie(x=values, labels=labels, autopct='%1.1f%%')
        plt.title(name)
        plt.savefig(f'image_dump/{name} - pie chart.png', dpi=100)
        plt.show()

    def correlation_matrix(self, circle_mode=True, *, name, period='1y'):

        assets = [asset.ticker for asset in self.asset_list]

        correlation_matrix_generator(securities=assets, period=period, visual=True, img_name=name,
                                     interval='1d', circle_mode=circle_mode)



