#!/usr/bin/python3
'''code for a rectangle and methods: (based on 0-rectangle.py)'''


class Rectangle():
    '''Class with Private instance attributes'''

    def __init__(self, width=0, height=0):
        '''
        Initialization
        Args:
            width: how wide rect is -private instance attribute
            height:how height rect is -private instance attribute
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method to retrieve attribute - width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method
        Args:
            value: set width of the rect
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter method to retrieve attribute - height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method
        Args:
            value: set height of the rect
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
