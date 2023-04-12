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

    def to_json(self):
        '''Returns the dictionary description of object'''
        return self.__dict__
