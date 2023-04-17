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

    def __str__(self):
        '''
        overloading __str__ method from rectangle
        returns [Square] (<id>) <x>/<y> - <size>
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
