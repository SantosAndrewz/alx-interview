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
    is_prime = []
    sieve_out = [True] * (n + 1)

    for x in range(2, n + 1):
        if (sieve_out[x]):
            is_prime.append(x)
            for y in range(x, n + 1, x):
                sieve_out[y] = False

    return is_prime


def isWinner(x, nums):
    """
    determines the winner of the prime game.

    Args:
        x (int): Number of rounds of the prime game.
        nums (int): array of maximumum values of primes in each round.
    Returns:
        str: Name of the winner or None if winner can not be determined.
    """

    if x < 1 or not nums:
        return None

    wins_ben = 0
    wins_maria = 0

    for y in range(x):
        is_prime = determine_primes(nums[y])
        if len(is_prime) % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None
