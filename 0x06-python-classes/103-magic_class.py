#!/usr/bin/python3
'''Magic class based off Python Bytecode'''
import math


class MagicClass:
    '''Magic class'''
    def __init__(self, radius=0):
        '''Magic class initialization'''
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''Magic class - area circle'''
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        '''Magic - circle circumference '''
        return 2 * math.pi * self.__radius
