#!/usr/bin/python3
'''Module: code for square
Based on 9-rectangle.py
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Class that inherits from Rectangle
    defines a geometrical square
    '''
    def __init__(self, size):
        '''
        Initializer method for Square class
        serves as a constructor for square
        '''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''
        compute area of square
        '''
        return self.__size ** 2
