#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(map(lambda key_val: (key_val[0], key_val[1] * 2),
                    a_dictionary.items()))
