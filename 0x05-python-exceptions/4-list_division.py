#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and returns a new list.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the new list.

    Returns:
        list: A new list with the divisions of the elements.

    """
    valid_types = [int, float]
    result = []
    for el in range(list_length):
        try:
            dividend = my_list_1[el]
            divisor = my_list_2[el]
            product = 0
            if type(dividend) not in valid_types or \
                    type(divisor) not in valid_types:
                print("wrong type")
            else:
                try:
                    product = dividend / divisor
                except ZeroDivisionError:
                    print("divided by 0")
                finally:
                    result.append(product)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
