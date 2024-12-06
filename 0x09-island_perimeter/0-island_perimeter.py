#!/usr/bin/python3
"""
Module defines a function- island_perimeter that retuns a perimeter of t
he island described in a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the 2D grid.
    Args:
        grid (list[list[int]]): grid of 0s and 1s. 1 for land and 0 for water.
    Returns:
        int: The perimeter of the island.
    """

    perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < num_rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < num_cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1
    return perimeter
