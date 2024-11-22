#!/usr/bin/python3
"""
Module for the function that rotates an n x n 2D matrix 90 degrees
clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an nxn 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list): 2D square matrix
    Return:
        None
    """
    x = len(matrix)
    for i in range(x):
        for j in range(i):
            temp_m = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp_m

    for i in range(x):
        for j in range(int(x / 2)):
            temp_m = matrix[i][j]
            matrix[i][j] = matrix[i][x-1-j]
            matrix[i][x-1-j] = temp_m
