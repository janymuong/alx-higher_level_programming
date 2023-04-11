#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''Module: code for rectangle
Based on 7-base_geometry.py
'''


class Rectangle(BaseGeometry):
    '''
    Class that inherits from BaseGeometry
    defines a rectangle
    '''
    def __init__(self, width, height):
        '''
        Initializer method for Rectangle class
        serves as a constructor for rectangle
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
