#!/usr/bin/python3
"""
Defines a Rectangular class
"""


class Rectangle:
    """
    A template of the rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
        Public instance of area of rectangle

        Return:
            Area of the rectangle
    """
    def area(self):
        return self.__height * self.__width

    """
        Public instance of area of rectangle

        Return:
            Area of the rectangle
    """
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle as an integer.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        :return: A string representation of the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method for the Rectangle class.

        Decreases the number of instances of the Rectangle class by 1.
        Prints a farewell message.

        Args:
            self: The instance of the Rectangle class.
        Returns:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the area of the larger rectangle.

        Parameters:
            rect_1 (Rectangle): The first rectangle object to compare.
            rect_2 (Rectangle): The second rectangle object to compare.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            int: The area of the larger rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if area_1 < area_2:
                return rect_2
            return rect_1
