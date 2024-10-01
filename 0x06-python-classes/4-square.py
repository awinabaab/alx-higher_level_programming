#!/usr/bin/python3
"""A class that defines a square
"""


class Square:
    """A class that defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square object with private attribute size

        Args:
            size (int): size of the Square object

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Gets the value of self.__size

        Returns: the value of self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets self.__size to a new value

        Args:
            value (int): new value for self.__size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of a Square object

        Returns: the area of the square object
        """

        return (self.__size ** 2)
