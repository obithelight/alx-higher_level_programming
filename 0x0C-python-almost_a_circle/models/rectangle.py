#!/usr/bin/python3
''' Represents a Python Module '''

from models.base import Base


class Rectangle(Base):
    ''' Defines a rectangle class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initialises the rectangle class '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def __width(self):
        ''' Retrieves the width '''
        return self.width

    @__width.setter
    def __width(self, value):
        ''' Sets the width '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    @property
    def __height(self):
        ''' Retrieves the height '''
        return self.height

    @__height.setter
    def __height(self, value):
        ''' Sets the width '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

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
        self.x = value

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
        self.y = value
