#!/usr/bin/python3
"""
Module calculates the fewest number of operations needed to result in
exactly n 'H' characters in the file.
"""


def minOperations(n):
    """
    Method calculates the minimum number of operations needed to result
    in exactly n 'H' characters.

    Parameters:
    n (int): Target number of 'H' characters.

    Returns:
    int: Fewest number of operations needed, or 0 if n is impossible to
    achieve.
    """

    if n <= 1:
        return 0

    operations_count = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations_count += factor
            n //= factor
        factor += 1
    return operations_count
