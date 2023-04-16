#!/usr/bin/python3
'''Module: code for base class: source for subclassing
'''


class Base():
    '''
    Base class: in progress...
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializer - constructor for objects'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
