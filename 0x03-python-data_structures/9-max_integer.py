#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    max_idx = len(my_list)

    if not my_list:
        return None

    if len(my_list) == 1:
        return my_list[0]

    for i in range(max_idx):
        if my_list[i] > max:
            max = my_list[i]
    return max
