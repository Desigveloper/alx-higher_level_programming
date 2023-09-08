#!/usr/bin/python3
"""Integer Addition Module"""


def add_integer(a, b=98):
    """
    Adds two integers
    Parameter:
    a(int): The first integer
    b (int): The second integer that defaults to 98 is no arg passes

    Returns:
    int: The sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
