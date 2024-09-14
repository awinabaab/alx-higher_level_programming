#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list_len = len(my_list)
    if idx < 0 or idx > my_list_len:
        return my_list

    for index in range(0, my_list_len):
        if index == idx:
            del my_list[index]
    return my_list
