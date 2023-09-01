#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print the integers from.
        x (int): The number of elements to access in `my_list`.

    Returns:
        int: The real number of integers printed.
    """

    count = 0
    try:
        for el in range(x):
            if type(my_list[el]) is int:
                print("{:d}".format(my_list[el]), end='')
                count += 1
        print()
    except TypeError:
        pass

    return count
