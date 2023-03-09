#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    av = sys.argv[1:]
    op = ["+", "-", "*", "/"]
    count = len(av)
    if count != 3:
        print("Usage: .100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif av[1] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(av[0])
        b = int(av[2])
        if av[1] is "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif av[1] is "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif av[1] is "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif av[1] is "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
