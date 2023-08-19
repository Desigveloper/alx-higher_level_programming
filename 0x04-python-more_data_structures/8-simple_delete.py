#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        # deletes the key-value pair from the dictionary
        del a_dictionary[key]

    return a_dictionary
