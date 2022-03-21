from scipy.stats import norm
from tools.options.option_pricing.european.analytic.utility import d_2
import numpy as np


def vega(x0, k, r, t, sigma, q):

    return k * np.exp(- r * t) * norm.pdf(d_2(x0, k, r, t, sigma, q)) * np.sqrt(t)
