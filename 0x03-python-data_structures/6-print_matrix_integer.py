#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            if col != 0:
                print(' ', end='')
            print('{:d}'.format(row[col]), end='')

        print()
