from tools.options.option_pricing.european.analytic.utility import d_1, d_2
from scipy.stats import norm
import numpy as np


def theta(x0, k, r, t, sigma, q):
    term_1 = -np.exp(-q * t) * x0 * norm.pdf(d_1(x0, k, r, t, sigma, q)) * sigma / (2 * np.sqrt(t))
    term_2 = -r * k * np.exp(-r * t) * norm.cdf(d_2(x0, k, r, t, sigma, q))
    term_3 = q * x0 * np.exp(-q * t) * norm.cdf(d_1(x0, k, r, t, sigma, q))

    return term_1 + term_2 + term_3
