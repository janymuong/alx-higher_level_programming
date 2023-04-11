#!/usr/bin/python3
'''Module for:
Class `MyInt` that inherits(uses) `int` as base class.
'''


class MyInt(int):
    '''
    Class that inherits props of the int class
    but with inverted == and != operators.
    '''

    def __eq__(self, other):
        '''Inverted == operator'''
        return int(self) != int(other)

    def __ne__(self, other):
        '''Inverted != op'''
        return int(self) == int(other)
