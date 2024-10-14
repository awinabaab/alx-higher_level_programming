#!/usr/bin/python3
"""2-is_same_class.py module
"""


def is_same_class(obj, a_class):
    """Checks if @obj is an instance of @a_class

    Args:
        obj (object): object of a class
        a_class: a class

    Returns:
        True: if @obj is an exact instance of @a_class
        False: if @obj is not an excat instance of @a_class
    """
    return (type(obj) is a_class)
