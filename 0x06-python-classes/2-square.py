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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
