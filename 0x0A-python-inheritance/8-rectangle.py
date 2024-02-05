#!/usr/bin/python3
''' Represents a Rectangle Module '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A rectangle class that inherits from BaseGeometry '''

    def __init__(self, width, height):
        ''' Initializes the rectangle instance '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
