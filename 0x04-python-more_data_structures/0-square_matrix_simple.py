#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''compute the square value of all integers of a matrix'''

    return [[row[i] ** 2 for row in matrix] for i in range(len(matrix))]
