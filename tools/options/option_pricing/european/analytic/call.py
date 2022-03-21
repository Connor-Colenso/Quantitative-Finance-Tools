from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_1, d_2
import numpy as np

# Calculate the value of a European call option.


def call(x0, k, r, t, sigma):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param sigma: Volatility of underlying asset.
    :return: Value of a European call option.
    """

    d_1_tmp = d_1(x0, k, r, t, sigma)
    d_2_tmp = d_2(x0, k, r, t, sigma)

    cum_norm_dist_1 = norm.cdf(d_1_tmp)
    cum_norm_dist_2 = norm.cdf(d_2_tmp)

    return cum_norm_dist_1 * x0 - cum_norm_dist_2 * k * np.exp(-r * t)
