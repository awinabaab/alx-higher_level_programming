#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if not my_list:
        return 0
    try:
        for y in range(0, x):
            print("{}".format(my_list[y]), end="")
        print()
    except IndexError:
        print()
        return y
    else:
        return (y + 1)
