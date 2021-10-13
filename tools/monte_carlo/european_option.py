import numpy as np
from tools.estimate_stock_price import estimate_stock_price


def call(k, n, x0, t, r, sigma, paths):
    """
    :param k: Strike price of call option.
    :param n: Number of steps per simulation.
    :param x0: Start value of underlying asset.
    :param t: Expiry time of option.
    :param r: Risk-free fixed interest rate.
    :param sigma: Volatility.
    :param paths: Number of GBM paths created.
    :return: Estimated value of the European call option.
    """

    end_prices = estimate_stock_price(n, x0, t, r, sigma, paths)
    end_prices = end_prices - k

    # Check if < 0 and set to 0 if so.
    end_prices = [i if i > 0 else 0 for i in end_prices]

    # We discount the price back in time.
    return np.mean(end_prices) * np.exp(- r * t)


def put(k, n, x0, t, r, sigma, paths):
    """
    :param k: Strike price of call option.
    :param n: Number of steps per simulation.
    :param x0: Start value of underlying asset.
    :param t: Expiry time of option.
    :param r: Risk-free fixed interest rate.
    :param sigma: Volatility.
    :param paths: Number of GBM paths created.
    :return: Estimated value of the European put option.
    """

    end_prices = estimate_stock_price(n, x0, t, r, sigma, paths)
    end_prices = k - end_prices

    # Check if < 0 and set to 0 if so.
    end_prices = [i if i > 0 else 0 for i in end_prices]

    # We discount the price back in time.
    return np.mean(end_prices) * np.exp(- r * t)
