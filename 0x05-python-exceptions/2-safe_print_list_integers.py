#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        return 0
    try:
        for y in range(0, x):
            try:
                print("{:d}".format(my_list[y]), end="")
            except ValueError:
                continue
        print()
    except (TypeError, IndexError):
        print()
        return (y - 1)
    else:
        return (y + 1)
