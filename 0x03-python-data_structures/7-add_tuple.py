#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    if not tuple_a and not tuple_b:
        return None

    for i in range(2):
        if not tuple_a or len(tuple_a) < 2:
            tuple_a += (0,)
        elif not tuple_b or len(tuple_b) < 2:
            tuple_b += (0,)
        tuple_c += (tuple_a[i] + tuple_b[i],)

    return tuple_c
