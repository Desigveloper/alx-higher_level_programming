#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()

    if not tuple_a:
        tuple_a = (0,)

    if not tuple_b:
        tuple_b = (0,)

    for i in range(2):
        if len(tuple_a) < 2:
            tuple_a += (0,)
        elif len(tuple_b) < 2:
            tuple_b += (0,)
        tuple_c += (tuple_a[i] + tuple_b[i],)

    return tuple_c
