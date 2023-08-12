#!/usr/bin/python3


def print_names():
    import hidden_4

    """
    Prints the names of the attributes in the `hidden_4` module.

    Parameters:
        None

    Returns:
        None
    """
    names = dir(hidden_4)

    for name in names:
        if not name.startswith('__'):
            print("{}".format(name), end="\n")


if __name__ == '__main__':
    print_names()
