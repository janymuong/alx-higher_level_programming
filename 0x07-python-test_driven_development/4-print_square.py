#!/usr/bin/python3
'''
Module: print a square
in string representation in terms of #
'''


def print_square(size):
    '''
    Prints a square with the character #.

    Args:
        size (int): size of the square.
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        print('#' * size)
