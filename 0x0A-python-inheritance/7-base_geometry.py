#!/usr/bin/python3
'''Module: code for base geometry
based on 6-base_geometry.py
'''


class BaseGeometry():
    '''
    Base class with methods for basic geometry
    '''
    def area(self):
        '''Method to calculate the area of a geometric shape'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method to validate the value of an integer
        '''

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
