#!/usr/bin/python3
''' A Module for Full Rectangle '''


SuperClass = __import__("7-base_geometry").BaseGeometry


class Rectangle(SuperClass):
    ''' Defines the rectangle class '''

    def __init__(self, width, height):
        ''' Initializes the rectangle instance '''

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' finds the area of rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' returns informal string representation '''
        return f"[Rectangle] {self.__width}/{self.__height}"
