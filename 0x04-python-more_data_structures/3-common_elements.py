#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Use a list comprehension to create a new set containing 
	# the common elements
    common_set = {el for el in set_1 if el in set_2}

    return common_set
