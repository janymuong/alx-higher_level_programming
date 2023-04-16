#!/usr/bin/python3
'''Module: code for base class - source for subclassing
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class: represents a rectangle
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializer - constructor for rectangle'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # getter amd setter for height and width
    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter method for width'''
        self.__width = value

    @property
    def height(self):
        '''getter for height/returns (private)__height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height/sets priavte attr'''
        self.__height = value

    # getter amd setter for private attribute x
    @property
    def x(self):
        '''getter for/returns private attr x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x'''
        self.__x = value

    # getter amd setter for private attribute y
    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y/set y to value arg'''
        self.__y = value
