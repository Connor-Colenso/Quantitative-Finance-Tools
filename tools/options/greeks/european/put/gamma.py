from tools.options.greeks.european.call.gamma import gamma as gamma_call


def gamma(x0, k, r, t, sigma, q):

    return gamma_call(x0, k, r, t, sigma, q)
