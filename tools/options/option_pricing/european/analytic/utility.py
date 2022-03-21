import numpy as np


def d_1(x0, k, r, sigma, t):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param sigma: Volatility of underlying asset.
    :return: d_1 parameter of European puts/calls.
    """

    return (np.log(x0 / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))


def d_2(x0, k, r, sigma, t):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param sigma: Volatility of underlying asset.
    :return: d_1 parameter of European puts/calls.
    """

    return d_1(x0, k, r, sigma, t) - sigma * np.sqrt(t)
