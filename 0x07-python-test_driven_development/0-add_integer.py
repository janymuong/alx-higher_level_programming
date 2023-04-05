#!/usr/bin/python3
'''Module for function that adds 2 integers.'''


def add_integer(a, b=98):
    '''
    Adds 2 integers

    Args:
        a (int or float): first integer argument
        b (int or float): second integer, init 98

    Raises:
        TypeError: If a or b is not an integer or a float

    Returns:
        int: a + b
    '''

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
