#!/usr/bin/python3
"""
N-Queens Solver
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """
    Recursive function to solve the N-Queens problem
    """
    # Base case: all queens are placed
    if col >= N:
        print_solution(board)
        return

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_nqueens(board, col + 1)
            board[row][col] = '.'

def print_solution(board):
    """
    Print the current configuration of the board
    """
    for row in board:
        print(" ".join(row))
    print()


# Main program
if __name__ == "__main__":
    # Get N from command line argument
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

    # Create an empty board
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0)
