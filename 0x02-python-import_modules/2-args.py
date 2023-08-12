#!/usr/bin/python3

def count_argv():
    from sys import argv

    i = 1
    arg_len = len(argv) - 1

    if arg_len == 0:
        print("{0} {1}.".format(arg_len, "arguments"))
    elif arg_len == 1:
        print("{0} {1}:".format(arg_len, "argument"))
    else:
        print("{0} {1}:".format(arg_len, "arguments"))

    while (i <= arg_len):
        print("{0}: {1}".format(i, argv[i]))
        i += 1


if __name__ == '__main__':
    count_argv()
