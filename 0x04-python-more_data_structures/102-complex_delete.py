#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = a_dictionary.copy()
    for key, val in new_dictionary.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary