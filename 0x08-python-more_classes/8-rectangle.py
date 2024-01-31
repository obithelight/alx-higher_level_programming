#!/usr/bin/python3
'''Module representing a rectangle'''


class Rectangle:
    '''Defines a rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initializes a rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Retrieves the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Retrieves the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Returns the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        '''Returns informal string representation of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''

        box = []
        for x in range(self.__height):
            [box.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != (self.__height - 1):
                box.append('\n')
        return ''.join(box)

    def __repr__(self):
        '''Returns official string reprentation of rectangle'''
        return "Rectangle({} {})".format(self.__width, self.__height)

    def __del__(self):
        '''Deletes the rectangle'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
        del self.__width, self.__height
