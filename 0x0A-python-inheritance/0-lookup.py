#!/usr/bin/python3
'''Module: `0-lookup`
lists all available attributes and methods of an object
'''


def lookup(obj):
    '''
    returns the list of available attributes and methods of an object
    '''

    return [attr for attr in dir(obj)]
