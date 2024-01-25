#!/usr/bin/python3
"""Module for class square"""


class Square:
    """Defines the square class"""
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
