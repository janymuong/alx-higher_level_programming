#!/usr/bin/python3
'''Module for:
Class `MyInt` that inherits(uses) `int` as base class.
Overrides == opeartor with != behavior.
'''


class MyInt(int):
    '''
    Class that inherits props of the int class
    but with inverted == and != operators.
    '''

    def __eq__(self, val):
        '''Inverted == operator'''
        return int(self) != int(val)

    def __ne__(self, val):
        '''Inverted != op'''
        return int(self) == int(val)
