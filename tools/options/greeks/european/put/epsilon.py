from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_1
import numpy as np


def epsilon(x0, k, r, t, sigma, q):

    return x0 * t * np.exp(-q * t) * norm.cdf(-d_1(x0, k, r, t, sigma, q))
