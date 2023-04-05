#!/usr/bin/python3
'''whoami - module for function: print name to stdout'''


def say_my_name(first_name, last_name=''):
    '''
    Prints "My name is <first name> <last name>".

    first_name (string): first parameter - string representing the first name.
    last_name (string): string representing the last name (optional).

    raises TypeError: If either first_name or last_name is not a string.

    return: None
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
