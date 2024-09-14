#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list[::-1]
    for item in sorted(my_list, reverse=True):
        print("{:d}".format(item))
