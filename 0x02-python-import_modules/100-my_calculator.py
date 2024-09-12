#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(sys.argv)
    operators = "+-*/"
    if argc < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if operator == '+':
                print("{:d} {} ".format(a, operator),
                      "{:d} = ".format(b),
                      "{:d}".format(add(a, b)))
                sys.exit(1)
            elif operator == '-':
                print("{:d} {} ".format(a, operator),
                      "{:d} = ".format(b),
                      "{:d}".format(sub(a, b)))
                sys.exit(1)
            elif operator == '*':
                print("{:d} {} ".format(a, operator),
                      "{:d} = ".format(b),
                      "{:d}".format(mul(a, b)))
                sys.exit(1)
            elif operator == '/':
                print("{:d} {} ".format(a, operator),
                      "{:d} = ".format(b),
                      "{:d}".format(div(a, b)))
                sys.exit(1)
