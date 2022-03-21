from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_1
import numpy as np


def delta(x0, k, r, t, sigma, q):

    return -np.exp(-q * t) * norm.cdf(-d_1(x0, k, r, t, sigma, q))
