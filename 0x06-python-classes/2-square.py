#!/usr/bin/python3
"""A class that defines a square and initiliazes its size
   with a private attribute
"""


class Square:
    """A class that defines a square
    """

    def __init__(self, size=0):
        """Initializes a private instance field.

        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
