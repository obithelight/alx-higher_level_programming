#!/usr/bin/python3
"""A module for Square Class"""


class Square:
    """Defines the Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the class
        Args:
            size (int) - private instance attribute
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
            or not all(isinstance(item, int) for item in value) \
                or not all(item >= 0 for item in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        result = self.size ** 2
        return result

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print()
        else:
            for item in range(self.position[1]):
                print()
            for item in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
