#!/usr/bin/python3
'''Module for: function that divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix.
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): A number to divide all elements of the matrix.

    Returns:
        A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
                    or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
        TypeError: If each row of the matrix is not of the same size.
    '''
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a '
                        'matrix (list of lists) of integers/floats')

    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError('matrix must be a '
                        'matrix (list of lists) of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    return [[round(num / div, 2) for num in row] for row in matrix]
