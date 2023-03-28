#!/usr/bin/python3
'''class that can be instantitiated'''


class Square():
    '''class that defines a square with optional size'''

    def __init__(self, size=0):
        '''
        Initialization
        Args:
            size: the size of the square -private instance attribute
        '''
        self.__size = size

    @property
    def size(self):
        '''Getter method to retrieve attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method
        Args:
            value: the size of the square -private instance attribute
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''return the current square area'''
        return self.__size ** 2
