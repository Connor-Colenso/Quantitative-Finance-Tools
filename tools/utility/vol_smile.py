import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# TODO: 3D Volatility smile, with Z axis being option expiries.
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
    plt.title(f'Volatility smile for {ticker} options expiring on {expiry} as of {datetime.today().strftime("%Y-%m-%d")}')
    plt.xlabel('Strike Price')
    plt.ylabel('Implied Volatility')

    plt.savefig(f'image_dump/vol-smile-{ticker}.png', dpi=1200)

    plt.show()
