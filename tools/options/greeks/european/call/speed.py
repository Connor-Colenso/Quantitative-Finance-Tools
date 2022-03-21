from tools.options.option_pricing.european.analytic.utility import d_1
from tools.options.greeks.european.call.gamma import gamma
import numpy as np


def speed(x0, k, r, t, sigma, q):

    return -(gamma(x0, k, r, t, sigma, q) / x0) * (d_1(x0, k, r, t, sigma, q) / (sigma * np.sqrt(t)) + 1)
