from tools.options.greeks.european.call.vega import vega as vega_call


def vega(x0, k, r, t, sigma, q):

    return vega_call(x0, k, r, t, sigma, q)