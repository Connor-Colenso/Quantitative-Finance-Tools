import numpy as np


def d_1(x0, k, r, sigma, t, q):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param sigma: Volatility of the underlying asset.
    :param t: Time to option expiry.
    :param q: Continuous dividend yield over t.
    :return: d_1 parameter of European puts/calls.
    """

    return (np.log(x0 / k) + (r - q + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))


def d_2(x0, k, r, sigma, t, q):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param sigma: Volatility of the underlying asset.
    :param t: Time to option expiry.
    :param q: Continuous dividend yield over t.
    :return: d_2 parameter of European puts/calls.
    """

    return d_1(x0, k, r, sigma, t, q) - sigma * np.sqrt(t)
