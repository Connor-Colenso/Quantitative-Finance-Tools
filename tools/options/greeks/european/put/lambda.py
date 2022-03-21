from tools.options.greeks.european.put.delta import delta
from tools.options.option_pricing.european.analytic.put import put


# Namespace overlap with lambda keyword, hence:
def opt_lambda(x0, k, r, t, sigma, q):
    return delta(x0, k, r, t, sigma, q) * x0 / put(x0, k, r, t, sigma, q)
