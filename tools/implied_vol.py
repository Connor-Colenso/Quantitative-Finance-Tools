from tools.options.option_pricing.european.analytic.call import call as analytic_call
from tools.options.option_pricing.european.analytic.put import put as analytic_put



def call(x0, k, r, t, c):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param c: Call option price.
    :return: Implied volatility of the option.
    """

    # Calculates the implied volatility (IV) of an option.
    # if the value is less than 1000%.

    # Uses a standard bisection method.

    # Set the bounds of the region we will search.
    a = 0.00001
    b = 10

    # Standard bisection method, we search until the root is
    # within an error of 0.0001.
    while (b - a) > 0.0001:

        m = (a + b) / 2  # Mid-point calculation.

        # Determine if we are above or below the root.
        t1 = (analytic_call(x0, k, r, t, a) - c) * (analytic_call(x0, k, r, t, m) - c)

        if t1 < 0:
            b = m
        else:
            a = m

    # Return the midpoint of our found region.
    return (a + b) / 2


def put(x0, k, r, t, p):
    """
    :param x0: Spot price.
    :param k: Strike price.
    :param r: Fixed interest rate over t.
    :param t: Time to option expiry.
    :param p: Put option price.
    :return: Implied volatility of the option.
    """

    # Calculates the implied volatility (IV) of an option
    # if the value is less than 1000\%.

    # Uses a standard bisection method.

    # Set the bounds of the region we will search.
    a = 0.00001
    b = 10

    # Standard bisection method, we search until the root is
    # within an error of 0.0001.
    while (b - a) > 0.0001:

        m = (a + b) / 2  # Mid-point calculation.

        # Determine if we are above or below the root.
        t1 = (analytic_put(x0, k, r, t, a) - p) * (analytic_put(x0, k, r, t, m) - p)

        if t1 < 0:
            b = m
        else:
            a = m

    # Return the midpoint of our found region.
    return (a + b) / 2
