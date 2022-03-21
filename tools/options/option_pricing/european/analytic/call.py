from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_1, d_2
import numpy as np

# Calculate the value of a European put option.


def call(x0, k, r, t, sigma, q):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param sigma: Volatility of the underlying asset.
    :param t: Time to option expiry.
    :param q: Continuous dividend yield over t.
    :return: Value of a European call option.
    """

    cum_norm_1 = norm.cdf(d_1(x0, k, r, sigma, t, q))
    cum_norm_2 = norm.cdf(d_2(x0, k, r, sigma, t, q))

    return np.exp(- r * t) * (x0 * np.exp((r - q) * t) * cum_norm_1 - k * cum_norm_2)
