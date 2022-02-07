from stochastics.brownian_motion import brownian_motion
import numpy as np


def geometric_brownian_motion(n, x0, t, mu, sigma):  # GBM Generator.
    """
    :param n: Number of steps.
    :param x0: Start value of GBM.
    :param t: End time of GBM.
    :param mu: Drift.
    :param sigma: Volatility.
    :return: Geometric Brownian motion of N steps.
    """

    # Using Brownian motion function.
    B = brownian_motion(n)

    # We generate N values of t equally spread on [0,T].
    t = np.linspace(0, t, n)

    # Putting it all together.
    gbm = x0 * np.exp((mu - 0.5 * sigma ** 2) * t + B * sigma)

    return gbm
