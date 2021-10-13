import numpy as np


def stochastic_integration(x, p):
    """
    :param x: Stochastic process.
    :param p: The point at which to integrate from within the interval.
    :return: The integrals value.

    Stochastic integration function, this will integrate B
    from 0 to T where T is defined as part of the function
    to generate Brownian motion.

    p = 0 is the ito integral.
    p = 0.5 is the stratonovich integral.

    0 ≤ p ≤ 1, 1dp only.
    """

    p = int(p * 10)

    if p == 10:

        # Does an 'upper' integral.

        skips = x[1:]
        diff = np.diff(x)

    elif p == 0:

        # Does a 'lower' integral.
        skips = x[:-1]
        diff = np.diff(x)

    else:

        # Takes every 10th value from B starting at p.
        skips = np.array(x[p::10])[:-1]

        # Takes the difference of every 10th point.
        diff = np.diff(x[::10], 1)

    # Put all our values together.
    return sum(skips * diff)
