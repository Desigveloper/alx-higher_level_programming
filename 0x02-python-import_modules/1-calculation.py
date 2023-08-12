#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as calculator

    a = 10
    b = 5
    sum = calculator.add(a, b)
    sub = calculator.sub(a,b)
    mul = calculator.mul(a, b)
    div = calculator.div(a, b)

    print("{0} + {1} = {2}".format(a, b ,sum))
    print("{0} - {1} = {2}".format(a, b ,sub))
    print("{0} * {1} = {2}".format(a, b ,mul))
    print("{0} / {1} = {2}".format(a, b ,div))
