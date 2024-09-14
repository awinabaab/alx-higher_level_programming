#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list_len = len(my_list)
    max_int = 0
    if my_list_len == 0:
        return None

    for idx in range(0, my_list_len):
        if my_list[idx] > max_int:
            max_int = my_list[idx]

    return max_int
