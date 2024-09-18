#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list and (search in my_list):
        new_list = my_list[:]
        for idx in range(0, len(new_list)):
            if new_list[idx] == search:
                new_list[idx] = replace
        return (new_list)
