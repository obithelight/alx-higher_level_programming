#!/usr/bin/python3
''' Module Representing a Square '''


class Square:
    ''' Defines a Square Class '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Constructor
        Args:
            size (int) - size of the new square
            position (int, int) - position of the new square
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' retrieves the size of the new square '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' sets the size of the new square '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' retrieves the position of the new square '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' sets the position of the new square '''
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        ''' returns the current square area '''
        return self.size ** 2

    def my_print(self):
        ''' prints in stdout the square with the character # '''
        if self.size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
