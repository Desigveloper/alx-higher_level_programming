#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    This class represents a magic circle.

    Attributes:
        __radius (int or float): The radius of the circle.

    Methods:
        __init__(self, radius): Initializes a MagicClass instance.
        area(self): Calculates and returns the area of the circle.
        circumference(self): Calculates and returns the circumference.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If `radius` is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
