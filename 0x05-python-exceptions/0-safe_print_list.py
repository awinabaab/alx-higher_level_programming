#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        return 0
    try:
        for idx in range(0, x):
            try:
                print("{}".format(my_list[idx]), end="")
            except (IndexError, TypeError, KeyError):
                idx -= 2
        print()
    finally:
        return (idx + 1)
