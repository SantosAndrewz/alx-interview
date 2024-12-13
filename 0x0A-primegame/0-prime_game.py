#!/usr/bin/python3
"""
Module for determining the winner of the game of prime numbers.
"""


def determine_primes(n):
    """
    Determines list of primes up to n.

    Args:
        n (int): maximum value of the primes obtained.

    Returns:
        tuple: a list showing if numbers are prime and
        a list of cumulative prime counts.
    """

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for x in range(2, int(n**0.5) + 1):
        if is_prime[x]:
            for y in range(x * x, n + 1, x):
                is_prime[y] = False

    prms_to = [0] * (n + 1)
    for x in range(1, n + 1):
        prms_to[x] = prms_to[x - 1] + (1 if is_prime[x] else 0)
    return is_prime, prms_to


def isWinner(x, nums):
    """
    determines the winner of the prime game.

    Args:
        x (int): Number of rounds of the prime game.
        nums (int): array of maximumum values of primes in each round.
    Returns:
        str: Name of the winner or None if winner can not be determined.
    """

    if x < 1 or not nums or any(n < 1 for n in nums):
        return None

    max_n = max(nums)
    is_prime, _ = determine_primes(max_n)

    wins_ben = 0
    wins_maria = 0

    for n in nums:
        pm = [p for p in range(2, n + 1) if is_prime[p]]
        turn = 0

        while pm:
            prime_now = pm.pop(0)
            pm = [p for p in pm if p % prime_now != 0]
            turn = 1 - turn

        if turn == 1:
            wins_maria += 1
        else:
            wins_ben += 1
    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None
