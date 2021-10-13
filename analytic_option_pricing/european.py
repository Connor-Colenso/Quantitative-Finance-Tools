import numpy as np
from scipy.stats import norm


# Calculate the value of a European call option.
def c_bs(x0, k, r, t, sigma):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param sigma: Volatility of underlying asset.
    :return: Value of a European call option.
    """

    # Evaluate values d1, d2.
    d1 = (np.log(x0 / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)

    N1 = norm.cdf(d1)
    N2 = norm.cdf(d2)

    return N1 * x0 - N2 * k * np.exp(-r * t)


def p_bs(x0, k, r, t, sigma):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param sigma: Volatility of underlying asset.
    :return: Value of a European put option.
    """

    # Evaluate values d1, d2.
    d1 = (np.log(x0 / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)

    N1 = norm.cdf(-d2)
    N2 = norm.cdf(-d1)

    return k * np.exp(-r * t) * N1 - x0 * N2
