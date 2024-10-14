#!/usr/bin/python3
"""lookup dunction module
"""


def lookup(obj):
    """A function that returns a list of available
     attributes and methods of an object

    Args:
        obj (object): instance of a class

    Returns:
        returns a list of available
        attributes and methods of an obj
    """

    return (dir(obj))
