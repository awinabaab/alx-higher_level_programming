#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        result = 0
        uniq_list = set(my_list)
        for num in uniq_list:
            result += num
        return result
