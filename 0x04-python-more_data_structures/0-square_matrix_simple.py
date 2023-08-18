#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    _matrix = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]

    # Use map to square each element in the input matrix
    # and store the result in the corresponding position in the result matrix
    for i in range(len(matrix)):
        _matrix[i] = list(map(lambda x: x ** 2, matrix[i]))

    return _matrix
