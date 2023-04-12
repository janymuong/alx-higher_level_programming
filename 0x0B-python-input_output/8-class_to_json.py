#!/usr/bin/python3
'''
Module: Returns the dictionary description of object
'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structure (list,
    dictionary, string, integer and boolean) for JSON serialization of an
    object.

    args:
        obj (object): an instance of a Class.
    '''

    return obj.__dict__
