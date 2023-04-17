#!/usr/bin/python3
'''Module: code for Square subclass of Rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class: represents a geometrical square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        initializer - constructor for Square class
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for size/square'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size/square'''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        overloading __str__ method from rectangle
        returns [Square] (<id>) <x>/<y> - <size>
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        '''
        *args, **kwargs for arbitrary positional arguments, keyworded args
        public method that assigns an argument to each attribute

        args:
            *args: a list of arguments
            **kwargs: a dictionary of keyword arguments
        '''
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
