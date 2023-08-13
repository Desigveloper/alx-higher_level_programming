#!/usr/bin/python3

def handle_operation():
    import calculator_1 as calc
    from sys import argv


    """

    imports all functions from the file calculator_1.py and handles basic operations.

    Parameters:
        None

    Returns:
        1 if error
    """

    args_len = len(argv) - 1

    if not args_len == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        print("{0} + {1} = {2}".format(a, b, calc.add(a, b)))
    elif operator == '-':
        print("{0} - {1} = {2}".format(a, b, calc.sub(a, b)))
    elif operator == '*':
        print("{0} * {1} = {2}".format(a, b, calc.mul(a, b)))
    elif operator == '/':
        print("{0} / {1} = {2}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1



if __name__ == '__main__':
    handle_operation()
