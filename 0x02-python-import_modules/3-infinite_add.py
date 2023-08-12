#!/usr/bin/python3

def sum_args():
    from sys import argv
    sum = 0
    args_len = len(argv) - 1
    i = 1

    while i <= args_len:
        sum += int(argv[i])
        i += 1

    print("{0}".format(sum))


if __name__ == "__main__":
    sum_args()
