#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    products_dict = {}

    for key, value in a_dictionary.items():
        products_dict[key] = value * 2

    return products_dict
