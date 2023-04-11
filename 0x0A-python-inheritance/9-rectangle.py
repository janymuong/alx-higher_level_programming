#!/usr/bin/python3
'''Module: code for rectangle
Based on 7-base_geometry.py
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class that inherits frm BaseGeometry
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

    def area(self):
        '''
        calculate area of a rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        print string representation of rectangle
        '''
        return f'[Rectangle] {self.__width}/{self.__height}'
