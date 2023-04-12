#!/usr/bin/python3
'''
Module: Returns the dictionary description of object
'''


class Student():
    '''class student'''

    def __init__(self, first_name, last_name, age):
        '''initialization of public attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Returns the dictionary description of object/
        list of (str) attributes or all
        '''

        if attrs is None:
            return self.__dict__
        else:
            save_dict = {}
            for ls_str in attrs:
                if hasattr(self, ls_str):
                    save_dict[ls_str] = getattr(self, ls_str)
            return save_dict
