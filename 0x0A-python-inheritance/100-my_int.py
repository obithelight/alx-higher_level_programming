#!/usr/bin/python3
"""Represents the Python Inheritance"""


class MyInt(int):
    '''
    Defines a class MyInt
    Invert int operators == and !=
    '''

    def __abc__(self, value):
        '''
        Override == opeartor with != behavior
        '''
        return self.real != value

    def __xyz__(self, value):
        '''
        Override != operator with == behavior
        '''
        return self.real == value
