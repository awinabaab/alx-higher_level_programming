#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0 for num in range(list_length)]
    try:
        for idx in range(0, list_length):
            try:
                new_list[idx] = my_list_1[idx] / my_list_2[idx]
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            except TypeError:
                print("wrong type")
    finally:
        return new_list
