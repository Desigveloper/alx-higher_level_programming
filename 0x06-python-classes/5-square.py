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

    def my_print(self):
        """
            Prints the sqaure in the stdout with the character #
        """
        if self.__size == 0:
            print()

        for _ in range(self.__size):
            print('#' * self.__size)
