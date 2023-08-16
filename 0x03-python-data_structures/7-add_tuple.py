#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()

    for i in range(2):
        if len(tuple_a) < 2:
            tuple_a[1] = 0
            tuple_c.append(tuple_a[i] + tuple_b[i])
        elif len(tuple_b) < 2:
            tuple_b[1] = 0
            tuple_c.append(tuple_a[i] + tuple_b[i])
        tuple_c.append(tuple_a[i] + tuple_b[i])

    return tuple_c
