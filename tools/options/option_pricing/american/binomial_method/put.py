import numpy as np
import tools.options.option_pricing.american.binomial_method.payoffs as payoffs


def binomial_method(sigma, M, T, S, r, K, D=0, method=1):
    """
    :param sigma: Volatility of the underlying.
    :param M: Number of periods the binomial method will cover.
    :param T: Time till expiry (in years).
    :param S: Underlying price at time t=0.
    :param r: Interest rate.
    :param K: Strike price.
    :param D: Continuous dividend yield over the lifetime of the option.
    :param method: Specifies which binomial method to utilise. 1 for = 0.5 and 2 for alternative.
    :return: Price of the option.
    """

    # Initial setup variables.
    dt = T / (M - 1)
    matrix = np.zeros(shape=(M, M)) + S

    if method == 1:

        u = np.exp(r * dt) * (1 + np.sqrt(np.exp(sigma ** 2 * dt) - 1))
        d = np.exp(r * dt) * (1 - np.sqrt(np.exp(sigma ** 2 * dt) - 1))
        p = 0.5

    elif method == 2:

        u = np.exp(sigma * np.sqrt(dt))
        d = 1/u
        p = (np.exp((r - D) * dt) - d) / (u - d)

    else:

        raise Exception(f'Invalid method selected for binomial method (method={method})')

    # Iterate over the matrix of values and store the binomial tree.
    for i in range(M):

        for j in range(i + 1, M):
            matrix[i][j] = S * u ** (j - i)

    for i in range(M):
        matrix[i][i:] *= d ** i

    # We now designate a payoff matrix, this will hold the associated value of the option at all time steps.
    payoff_matrix = np.zeros(shape=(M, M))

    # Iterates over the final column values to generate payoff info.
    for i in range(M):
        payoff_matrix[i, M - 1] = payoffs.american_put_payoff(matrix[i, M - 1], K)

    # Iterate from the 2nd furthest column at the lowest value first.
    for col in range(M - 2, -1, -1):

        # Prevents iterating over empty values in payoff_matrix.
        for row in range(0, col + 1):
            val_1 = payoffs.american_put_payoff(matrix[row, col], K)
            val_2 = (p * payoff_matrix[row, col + 1] + (1 - p) * payoff_matrix[row + 1, col + 1]) * np.exp(-r * dt)

            # Take the greatest value of the two payoffs to prevent arbitrage.
            payoff_matrix[row, col] = max(val_1, val_2)

    return payoff_matrix[0, 0]
