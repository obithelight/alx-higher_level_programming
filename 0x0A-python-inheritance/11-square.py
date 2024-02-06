#!/usr/bin/python3
'''Represents A Module for Square 2'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines a Square Class that inherits from a Rectangle Class'''

    def __init__(self, size):
        '''Initializes the square'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''Calculates the area of square'''
        return self.__size ** 2

    def __str__(self):
        '''Informal string representation of square'''
        return f"[Square] {self.__size}/{self.__size}"
