#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for idx in range(0, x):
            print("{}".format(my_list[idx]), end="")
            printed += 1
    except IndexError:
        pass
    print()
    return printed
