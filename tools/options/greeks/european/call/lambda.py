from tools.options.greeks.european.call.delta import delta
from tools.options.option_pricing.european.analytic.call import call


# Namespace overlap with lambda keyword, hence:
def opt_lambda(x0, k, r, t, sigma, q):
    return delta(x0, k, r, t, sigma, q) * x0 / call(x0, k, r, t, sigma, q)
