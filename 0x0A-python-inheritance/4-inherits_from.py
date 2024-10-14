#!/usr/bin/python3
"""4-inherits_from.py module
"""


def inherits_from(obj, a_class):
    """Checks if @obj is an instance of a class that inherited
    directly or indirectly from @a_class

    Args:
        obj (object): an object
        a_class (class): a class

    Returns:
        True: if @obj is an instance of a class that inherited
        directly or indirectly from @a_class

        False: if @obj not is an instance of a class that inherited
        directly or indirectly from @a_class
    """

    return (isinstance(obj, a_class) and type(obj) is not a_class)
