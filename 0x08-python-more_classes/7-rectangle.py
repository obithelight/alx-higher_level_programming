#!/usr/bin/python3
'''Module representation for rectangle'''


class Rectangle:
    '''Defines a rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Initializes the class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Retrieves the rectangle's width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the rectangle's width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Retrieves the rectangle's height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the rectangle's height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Returns the area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''Returns informal string representation of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''

        items = []
        for i in range(self.__height):
            [items.append(Rectangle.print_symbol) for j in range(self.__width)]
            if i != (self.__height - 1):
                items.append('\n')
        return ''.join(items)

    def __repr__(self):
        '''Returns official string representation of rectangle'''
        return "Rectangle({} {})".format(self.__width, self.__height)

    def __del__(self):
        '''Deletes the rectangle'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
        del self.__width, self.__height
