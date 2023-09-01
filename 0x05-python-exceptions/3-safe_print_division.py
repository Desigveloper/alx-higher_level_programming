#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides 2 integers and prints the result

    Args:
        a and b: the 2 integers to be divided

    Returns:
        The result of division or None
    """

    try:
        result = a / b
    except Exception as e:
        result =  None
    finally:
        print("Inside result: {}".format(result))
