#!/usr/bin/python3
"""Module for Square Class"""


class Square:
    """Defines a Square Class based on 3-square.py"""
    def __init__(self, size=0):
        """
        Initializes a new square
        Args:
            size (int) - private instance attribute
        """
        self.size = size

    @property
    def size(self):
        """Gets and sets the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        result = self.__size ** 2
        return result
