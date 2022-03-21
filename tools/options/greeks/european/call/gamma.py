from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_2
import numpy as np


def gamma(x0, k, r, t, sigma, q):

    return k * np.exp(-r * t) * norm.pdf(d_2(x0, k, r, t, sigma, q)) / (x0 ** 2 * sigma * np.sqrt(t))
