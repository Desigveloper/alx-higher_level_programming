#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            upper_case = chr(ord(letter) - 32)
        else:
            upper_case = letter
        print(f'{upper_case}'.format(upper_case), end='')
    print("")
