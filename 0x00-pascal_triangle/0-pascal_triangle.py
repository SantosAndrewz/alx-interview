#!/usr/bin/python3
"""
A module for writing a pascal's triangle
"""


def pascal_triangle(n):
    """
    Creates a list of integers representing the Triangle of n
    Returns: empty list if n <= 0
    """

    x = {}
    if n <= 0:
        return x
    x = [[1]]
    for a in range(1, n):
        temp = [1]
        for b in range(len(x[a - 1]) - 1):
            c = x[a - 1]
            temp.append(x[a - 1][b] + x[a - 1][b + 1])
        temp.append(1)
        x.append(temp)
    return x
