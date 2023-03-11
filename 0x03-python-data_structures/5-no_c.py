#!/usr/bin/python3
def no_c(my_string):
    '''I live in Chicago but without cC'''

    return ''.join([c for c in my_string if c not in 'cC'])
