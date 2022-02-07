import tools.option_pricing.american_options.binomial_method.american_call_option as american_call
import tools.option_pricing.american_options.binomial_method.american_put_option as american_put
import tools.option_pricing.american_options.binomial_method.american_chooser_option as american_chooser
from tools.gbm_estimate_parameters import gbm_estimate_parameters
import yfinance
import matplotlib.pyplot as plt
from tools.equities.price_path import price_path


def main():
    # price = american_chooser.binomial_method(sigma=0.3, M=4, T=1.5, S=100, r=0.05, K=10, method=1)
    # print(price)

    ticker = 'MSFT'
    model_start_date = '2015-01-01'
    model_end_date = '2018-01-01'
    exchange_name = 'NASDAQ'

    historical_data = yfinance.Ticker('MSFT').history(start='2013-01-01', end='2015-01-01')['Close']

    drift, vol = gbm_estimate_parameters(x=list(historical_data), t=len(historical_data) / 252)
    print(drift, vol)

    # tmp_series = price_path(ticker, model_start_date, model_end_date, drift, vol, exchange_name)
    #
    # for _ in range(4):
    #     tmp_series += price_path(ticker, model_start_date, model_end_date, drift, vol, exchange_name)
    #
    #
    # plt.plot(tmp_series / 5, color='red', label='Price projection')

    series = price_path(ticker, model_start_date, model_end_date, drift, vol, exchange_name)
    plt.plot(series, color='red', label='Price projection')

    plt.plot(yfinance.Ticker('MSFT').history(start=model_start_date, end=model_end_date)['Close'], color='green', label='Historical data')
    plt.plot(historical_data, color='blue', label='Sample data')

    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.title('MSFT Price Projection 2015-2018')
    plt.subplots_adjust(bottom=0.2)
    plt.savefig('TEST.png', dpi=1200)
    plt.show()


if __name__ == '__main__':
    main()
