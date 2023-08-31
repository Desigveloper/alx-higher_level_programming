#!/usr/bin/python3
"""
    This module defines a class representing a Square
"""


class Square:
    """Implementation of the Square
    """
    def __init__(self, size=0):
        """
            Initializes an instance of the Square class

            Args:
                size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
            Initializes the size of an instance

            Args:
                The value passed

            Raises:
                TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
            A pubic instance method representing area of Square

            Args:
                self - first param by convention of instance method

            Returns:
                the current square area
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.__size == other.size

    def __not_equal__(self, other):
        return self.__size != other.size

    def __grt__(self, other):
        return self.__size > other.size

    def __grt_or_eql__(self, other):
        return self.__size >= other.size

    def __lt__(self, other):
        return self.__size < other.size

    def __le__(self, other):
        return self.__size <= other.size
