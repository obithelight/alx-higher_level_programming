#!/usr/bin/python3
''' Module Representing a Square '''


class Square:
    ''' Defines a Square Class '''

    def __init__(self, size=0):
        '''
        Initializes a new square
        Args:
            size (int) - size of the new square
        '''
        self.size = size

    @property
    def size(self):
        ''' retrieves the size of the new square '''
        return (self.__size)

    @size.setter
    def size(self, value):
        ''' sets the size of the new square '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' returns the current square area '''
        return (self.size ** 2)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
