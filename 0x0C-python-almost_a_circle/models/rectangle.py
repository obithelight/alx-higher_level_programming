#!/usr/bin/python3
''' Represents a Python Module '''

from models.base import Base


class Rectangle(Base):
    ''' Defines a rectangle class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initialises the rectangle class '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' Retrieves the width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets the width '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' Retrieves the height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets the width '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def __x(self):
        ''' Retrieves x '''
        return self.x

    @__x.setter
    def __x(self, value):
        ''' Sets the width '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def __y(self):
        ''' Retrieves y '''
        return self.y

    @__y.setter
    def __y(self, value):
        ''' Sets y '''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
