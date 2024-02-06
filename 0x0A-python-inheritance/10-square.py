#!/usr/bin/python3
''' Represents a Square Module '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Defines a Square Class '''

    def __init__(self, size):
        ''' Initializes a square instance '''

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Calculates the area of a square '''
        return self.__size * self.__size
