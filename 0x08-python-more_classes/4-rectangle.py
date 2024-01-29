#!/usr/bin/python3
'''Module representing a rectangle'''


class Rectangle:
    '''Defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes a rectangle'''
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
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Defines the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Defines the rectangle perimeter'''
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''Returns informal string representation of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''

        items = []
        for a in range(self.__height):
            [items.append("#") for b in range(self.__width)]
            if a != (self.__height - 1):
                items.append("\n")
        return ''.join(items)

    def __repr__(self):
        '''Returns official string representation of the rectangle'''
        return "Rectangle({}, {})".format(self.__width, self.__height)
