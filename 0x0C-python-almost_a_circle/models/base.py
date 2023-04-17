#!/usr/bin/python3
'''Module: code for base class - source for subclassing
'''

import json


class Base():
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

    @classmethod
    def save_to_file(cls, list_objs):
        '''class method
        writes JSON string representation of instances to a file
        instances(subclassing Base)
        '''
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                obj_list = []
                for obj in list_objs:
                    obj_list.append(obj.to_dictionary())
                json_repr = cls.to_json_string(obj_list)
                f.write(json_repr)
