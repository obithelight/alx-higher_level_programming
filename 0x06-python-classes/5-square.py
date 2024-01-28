#!/usr/bin/python3
"""A module for Square Class"""


class Square:
    """Defines the Square Class"""
    def __init__(self, size=0):
        """
        Initializes the class
        Args:
            size (int) - private instance attribute
        """
        self.__size = size

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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
