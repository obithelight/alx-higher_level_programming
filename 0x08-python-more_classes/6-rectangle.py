#!/usr/bin/python3
'''Module representing a rectangle'''


class Rectangle:
    '''Defines a rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''
        Initializes the rectangle class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        '''Returns area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''Returns informal string representation of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''
        content = []
        for x in range(self.__height):
            [content.append('#') for y in range(self.__width)]
            if x != (self.__height - 1):
                content.append('\n')
        return ''.join(content)

    def repr(self):
        '''Returns official string representation of rectangle'''
        return "Rectangle({} {})".format(self.__width, self.__height)

    def __del__(self):
        '''Deletes the rectangle'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
        del self.__width, self.__height
