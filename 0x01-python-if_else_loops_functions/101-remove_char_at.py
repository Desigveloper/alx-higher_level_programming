#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ''
    i = 0
    j = 0

    for letter in str:
        i += 1

    while (j < i):
        if not j == n:
            new_str += str[j]
        j += 1

    return new_str
