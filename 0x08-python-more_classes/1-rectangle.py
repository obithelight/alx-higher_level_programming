#!/usr/bin/python3
'''A Module Representing a Class Rectangle'''


class Rectangle:
    '''Defines the Rectangle Class'''
    def __init__(self, width=0, height=0):
        '''
        Initializes the Rectangle Class
        Args:
            width (int) - width of the rectangle
            height (int) - height of the rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Gets the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the value for width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the value for height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
