#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    prints all integers in a given list

    Parameter:
        my_list - list to be printed

    Return:
        none
    """
    for el in my_list:
        print("{:d}".format(el))
