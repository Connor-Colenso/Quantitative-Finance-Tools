from tools.options.greeks.european.call.speed import speed as call_speed


def speed(x0, k, r, t, sigma, q):

    return call_speed(x0, k, r, t, sigma, q)