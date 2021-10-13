import numpy as np
from brownian_motion import geometric_brownian_motion


def estimate_stock_price(n, x0, t, mu, sigma, paths):
    """
    :param n: Number of steps.
    :param x0: Start value of GBM.
    :param t: End time of GBM.
    :param mu: Drift.
    :param sigma: Volatility.
    :param paths: Number of times to simulate the stock.
    :return: Estimated price of the stock.
    """

    end_prices = np.zeros(paths)

    # Calculate the end value of each path and take the average.
    for i in range(paths):
        end_prices[i] = geometric_brownian_motion(n, x0, t, mu, sigma)[-1]

    return end_prices
