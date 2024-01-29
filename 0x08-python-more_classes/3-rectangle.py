#!/usr/bin/python3
'''Module for representing a rectangle'''


class Rectangle:
    '''Defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes the Rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieves the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieves the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Defines the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Defines the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __set__(self):
        '''Returns string representation of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''

        box = []
        for x in range(self.__height):
            [box.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                    box.append('\n')
        return ("".join(box))
