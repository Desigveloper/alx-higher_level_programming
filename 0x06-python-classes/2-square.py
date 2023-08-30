#!/usr/bin/python3
"""
 This module defines a class representing a Square
"""


class Square:
    """Implementation of the Square
    """
    def __init__(self, size=0):
        """
            Initializes an instance of the Square classs
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
