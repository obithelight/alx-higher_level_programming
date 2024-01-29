#!/usr/bin/python3
'''A Module Representing a Rectangle Class'''


class Rectangle:
    '''Defines the Rectangle Class'''
    def __init__(self, width=0, height=0):
        '''
        Initializes the Rectangle Class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets the width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width of rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height of rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Defines the area of a rectangle class'''
        return self.__width * self.__height

    def perimeter(self):
        '''Defines the perimeter of a rectangle class'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
