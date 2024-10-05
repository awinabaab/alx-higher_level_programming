#!/usr/bin/python3
"""
A function that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds a and b

    Args:
        a (int) or (float): first number
        b (int) or (float): second number

    Raises:
        TypeError: if a or b is not an integer or a float

    Returns:
        int : addition of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
