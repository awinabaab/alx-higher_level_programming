#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x < 1:
        return 0
    try:
        for idx in range(0, x):
            print("{}".format(my_list[idx]), end="")
        print()
        return (idx + 1)
    except (IndexError, TypeError):
        print()
        return (idx)
