#!/usr/bin/python3
'''Module: code for base class - source for subclassing
'''

import json


class Base:
    '''
    Base class: represents the base of all other classes

    attributes:
        __nb_objects: private class attribute
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializer - constructor for objects'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method - for serialization
        returns the JSON string representation of a list of dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
