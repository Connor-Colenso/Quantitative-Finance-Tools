from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_2
import numpy as np


def rho(x0, k, r, t, sigma, q):

    return -k * t * np.exp(-r * t) * norm.cdf(-d_2(x0, k, r, t, sigma, q))
