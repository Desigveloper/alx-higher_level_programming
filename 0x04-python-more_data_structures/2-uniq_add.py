#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0

    # Use set to create a new list with unique elements before iterating
    for i in set(my_list):
        sum += i
    return sum
