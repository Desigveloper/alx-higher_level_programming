#!/usr/bin/python3

def element_at(my_list, idx):
    """
    retrieves an element from a list at an index

    Parameters:
        my_list, idx

    Return:
        none id index negative or out of range, else element value
    """

    if idx < 0 or idx >= len(my_list):
        return "None"
    else:
        return my_list[idx]
