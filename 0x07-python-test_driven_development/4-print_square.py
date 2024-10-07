#!/usr/bin/python3
"""A module that prints a square with the character #
"""


def print_square(size):
    """A function that prints a square with the character #

    Args:
        size (int): size of the square >= 0

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    print(((size * '#' + '\n') * size), end="")
