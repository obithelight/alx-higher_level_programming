#!/usr/bin/python3
'''Module representing a rectancle'''


class Rectangle:
    '''Defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes the rectangle'''
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
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Retrieves the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Defines area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Defines perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''Returns informal string documentation'''
        if self.__width == 0 or self.__height == 0:
            return ""

        elements = []
        for i in range(self.__height):
            [elements.append("#") for j in range(self.__width)]
            if i != (self.__height - 1):
                elements.append("\n")
        return "".join(elements)

    def __repr__(self):
        '''Returns official string documentation'''
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        '''Deletes the rectangle'''
        print('Bye rectangle...')
        del self.__width
        del self.__height
