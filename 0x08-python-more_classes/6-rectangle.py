#!/usr/bin/python3
'''code for a class rectangle and methods:'''


class Rectangle():
    '''Class with Private instance attributes, and class attributes'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''
        Initialization
        Args:
            width: how wide rect is -private instance attribute
            height:how height rect is -private instance attribute
        '''
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

    @property
    def width(self):
        '''Getter method to retrieve attribute - width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method
        Args:
            value: set width of the rect
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter method to retrieve attribute - height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method
        Args:
            value: set height of the rect
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Calculate area'''
        return self.__height * self.__width

    def perimeter(self):
        '''return perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        '''return string representation of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(map(lambda x: "#" * self.__width,
                             range(self.__height)))

    def __repr__(self):
        '''
        Return a string representation of the rectangle
        you can recreate the objec with it - using eval()
        '''
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        '''pseudo-destructor'''
        print(f'Bye rectangle...')

        type(self).number_of_instances -= 1
