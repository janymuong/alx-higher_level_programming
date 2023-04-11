#!/usr/bin/python3
'''Module: check for whether an object_is
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
'''


def inherits_from(obj, a_class):
    '''
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    '''

    return issubclass(type(obj), a_class) and type(obj) != a_class
