#!/usr/bin/python3
"""A Module for Square Class"""


class Square:
    """Defines a square based on 2-square.py"""

    def __init__(self, size=0):
        """
        Args:
            size (int) - private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance method
        """
        result = self.__size ** 2
        return result
