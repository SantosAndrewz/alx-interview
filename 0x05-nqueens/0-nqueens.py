#!/usr/bin/python3
'''
Module with a program for solving the N queens problem.
'''

import sys


def valid_place(queens, row, col):
    """
    Checks  if the queen can be safely placed at location (row, col)
    Args:
        queens: 2D list representing the chess board.
        row: row for the queen.
        col: column for the queen.
    Returns:
        boolean: True if the queen can be placed , false otherwise
    """

    if 1 in queens[row]:
        return False

    for x, y in zip(range(row, -1, -1), range(col, -1, -1))
        if queens[x][y] == 1:
            return False

    for x, y in zip(range(row, len(queens)), range(col, -1, -1)):
        if queens[x][y] == 1:
            return False

    return True

def solve_nqueens(queens, col):
    """
    Recursive backtracking solution finding all possible N-queens arrangements.
    Args:
        queens: 2D list representing the chess board.
        col: current column for placing the queen.
    """

    if col >= len(queens):
        display_solution(queens)
        return
    for row in range(len(queens)):
        if valid_place(queens, row, col):
            queens[row][col] = 1
            solve_nqueens(queens, col + 1)
            queens[row][col] = 0

def display_solution(queens):
    """
    Prints all the possible positions of the queens on the chess board.
    Args:
        queens: 2D list representing the chess board
    """
    sol = []
    for row in range(len(queens)):
        for col in range(len(queens)):
            if queens[row][col] == 1:
                sol.append([row, col])
    print(sol)

def nqueens(size):
    board = [[0] * size for _ in range(size)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    nqueens(N)
