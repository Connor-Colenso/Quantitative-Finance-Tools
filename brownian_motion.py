import numpy as np


def brownian_motion(n):  # Brownian Motion Generator with N steps.

    # Scale term.
    s = np.sqrt(1 / n)

    # This will generate N - 1 normally distributed values
    # scaled by sqrt(1/N), this is required because of the
    # discrete nature of the process.
    brownian_increments = np.random.normal(0, 1, n - 1) * s

    # This will cumulatively sum the values
    # of brownian_increments.
    # i.e. np.cumsum([1,2,3,4]) = [1,3,6,10]
    brownian_sum = np.cumsum(brownian_increments)

    # This simply makes sure that a 0 is inserted at
    # the beginning, hence why we use N-1 steps for
    # the brownian_increments.
    brownian_sum = np.insert(brownian_sum, 0, 0)

    return brownian_sum


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
