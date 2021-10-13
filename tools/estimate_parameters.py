import numpy as np


def estimate_parameters(x, t):
    """
    :param x: GBM data in a list.
    :param t: End time of GBM.
    :return: Tuple consisting of (mu, sigma)
    """

    # Required to make the estimate accurate.
    s = len(x) / t

    # Essentially the log difference.
    log_diff = np.diff(np.log(x))

    # Find sigma and mu, note that ddof = 1 indicates that we
    # divide by n-1 when taking the variance, if we do not
    # specify it will only divide by n.
    sigma = np.std(log_diff, ddof=1) * np.sqrt(s)
    mu = s * np.mean(log_diff) + 0.5 * sigma ** 2

    return mu, sigma
