#!/usr/bin/python3
"""3-is_kind_of_class.py module
"""


def is_kind_of_class(obj, a_class):
    """Checks if @obj is an instance of @a_class or
    is an instance of a class inherited by @a_class

    Args:
        obj (object): object
        a_class (class): a class

    Returns:
        True: if @obj is an instance of @a_class or
        is an instance of class inherited by @a_class

        False: if @obj is not an instance of @a_class or
        is not an instance of class inherited by @a_class
    """

    return (isinstance(obj, a_class))
