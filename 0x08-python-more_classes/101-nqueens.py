#!/usr/bin/python3
"""
Solves the N queens problem by placing N non-attacking queens on an
N×N chessboard.

Usage: nqueens N

Args:
    N (int): The size of the chessboard and the number of queens to be placed.
Returns:
    None

Raises:
    ValueError: If the user called the program with the wrong number
    of arguments, or if N is not a positive integer greater or equal to 4.

Prints:
    Every possible solution to the N queens problem, one solution per line.
    The format of each solution is as follows:
        - Each line represents a row on the chessboard.
        - The number on each line represents the column where the
        queen is placed in that row.
        - The numbering of the columns starts from 0.

Imports:
    sys: The sys module is imported to handle command line arguments.
"""

import sys


def solve_nqueens(N):
    def is_safe(board, row, col):
        """Check if there is a queen in the same column"""
        for i in range(row):
            if board[i] == col:
                return False

        """Check if there is a queen in the upper left diagonal"""
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i] == j:
                return False
            i -= 1
            j -= 1

        """Check if there is a queen in the upper right diagonal"""
        i = row - 1
        j = col + 1
        while i >= 0 and j < N:
            if board[i] == j:
                return False
            i -= 1
            j += 1

        return True

    def solve(board, row):
        if row == N:
            """Found a solution, add it to the solution list"""
            for i in range(N):
                print("[{}, {}]".format(i, board[i]), end=' ')
            print()
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    """Initialize the board"""
    board = [-1] * N

    """Start solving from the first row"""
    solve(board, 0)


if __name__ == "__main__":
    """Check if the correct number of arguments is provided"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

     """Check if N is a positive integer greater or equal to 4"""
    try:
        N = int(sys.argv[1])
        if not isinstance(N, int):
            raise ValueError
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """Check if N is a positive integer greater or equal to 4"""
    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
