#!/usr/bin/python3
'''Module: check for whether an object_is
exactly an instance of the specified class
'''


def is_kind_of_class(obj, a_class):
    '''
    check for whether an object is an instance of,
    or if the object is an instance of a class
    that inherited frm, the specified class
    '''

    return isinstance(obj, a_class)
