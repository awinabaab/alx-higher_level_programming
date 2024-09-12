#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    print("{:d} + ".format(a), "{:d} = ".format(b), "{:d}".format(add(a, b)))
    print("{:d} - ".format(a), "{:d} = ".format(b), "{:d}".format(sub(a, b)))
    print("{:d} * ".format(a), "{:d} = ".format(b), "{:d}".format(mul(a, b)))
    print("{:d} / ".format(a), "{:d} = ".format(b), "{:d}".format(div(a, b)))
