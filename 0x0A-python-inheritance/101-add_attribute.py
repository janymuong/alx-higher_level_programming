#!/usr/bin/python3
'''Module for:
function that tries add a new attribute to an object
'''


def add_attribute(obj, name, value):
    '''
    adds a new attribute to an object if it’s possible
    raises a TypeError exception otherwise
    '''

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
