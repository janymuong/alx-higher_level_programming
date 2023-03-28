#!/usr/bin/python3
'''class that can be instantitiated'''


class Square():
    '''class that defines a square with an attribute'''

    def __init__(self, size):
        '''
        Initialization
        Args:
            size: The size of the square
        '''
        self.__size = size
