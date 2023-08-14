#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = sum(range(4, 7))
        return add(add(a, b), c)
    else:
        return sub(a, b)

