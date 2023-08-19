#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Use set operations to find the elements present in only one set
    unique_set = (set_1 - set_2) | (set_2 - set_1)

    return unique_set
