#!/usr/bin/python3

"""
Divided all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists representing the matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2dp.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                or if each row of the matrix does not have the same size,
                or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    """Check if  matrix is a list of lists of integers or floats"""
    if not all(isinstance(row, list) and all(isinstance(el, (int, float))
            for el in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")

    """Check if each row of matrix has the same size"""
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    """Check if div is a number"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """Dividing each element of matrix by div"""
    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix
