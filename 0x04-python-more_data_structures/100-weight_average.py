#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        dividend = 0
        divisor = 0
        for num in list(map(lambda row: row[0] * row[1], my_list)):
            dividend += num
        for num in list(map(lambda row: row[1], my_list)):
            divisor += num
        return dividend / divisor
    else:
        return 0
