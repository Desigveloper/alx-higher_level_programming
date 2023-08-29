#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for el in my_list:
            if count < x:
                try:
                    print("{:d}".format(el), end='')
                    count += 1
                except ValueError:
                    pass
            else:
                break
        print()
        return count
    except TypeError:
        return count
