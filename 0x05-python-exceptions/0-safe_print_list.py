#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        return 0
    try:
        for y in range(0, x):
            print("{}".format(my_list[y]), end="")
        print()
    except (IndexError, TypeError, KeyError):
        print()
        return y
    else:
        return (y + 1)
