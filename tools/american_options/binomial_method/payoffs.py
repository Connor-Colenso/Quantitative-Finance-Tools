def american_call_payoff(S, K):
    return max(S - K, 0)


def american_put_payoff(S, K):
    return max(K - S, 0)


def american_chooser_payoff(S, K):

    if S <= K:

        return american_put_payoff(S, K)

    else:

        return american_call_payoff(S, K)
