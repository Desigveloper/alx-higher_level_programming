#!/usr/bin/python3

def handle_operation():
    """
    imports all functions from the file calculator_1.py
    and handles basic operations.

    Parameters:
        None

    Returns:
        1 if error
    """
    import calculator_1 as calc
    from sys import argv, exit

    args_len = len(argv) - 1

    if not args_len == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if op == '+':
            print("{0} + {1} = {2}".format(a, b, calc.add(a, b)))
        elif op == '-':
            print("{0} - {1} = {2}".format(a, b, calc.sub(a, b)))
        elif op == '*':
            print('{0} * {1} = {2}'.format(a, b, calc.mul(a, b)))
        elif op == '/':
            print("{0} / {1} = {2}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == '__main__':
    handle_operation()
