#!/usr/bin/python3
'''class OOP final'''


class Square():
    '''class that defines a square with optional size'''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialization
        Args:
            size: the size of the square -private instance attribute
            position: private instance attribute
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Getter method to retrieve attribute - position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter method
        Args:
            value: the size of the square -private instance attribute
        '''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''return the current square area'''
        return self.__size ** 2

    def my_print(self):
        '''
        print in stdout the square with the character #
        at the position
        '''
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()
