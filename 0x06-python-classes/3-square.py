#!/usr/bin/python3
"""A class that defines a square
"""


class Square:
    """A class that defines a square
    """
    def __init__(self, size=0):
        """Initializes an instance with size

        Args:
            size (int): size of instance(private)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of a square instance

        Returns: area of the square instance
        """
        return (self.__size ** 2)
