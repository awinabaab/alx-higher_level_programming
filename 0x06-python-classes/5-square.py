#!/usr/bin/python3
"""A class that defines a Square
"""


class Square:
    """A class that defines a Square
    """

    def __init__(self, size=0):
        """
        Initializes a Sqaure object with private attribute size

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
        """
        Gets the value of self.__size

        Returns: the value of self.__size
        """

        return (self.__size)

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the object

        Returns: the area of the object
        """

        return (self.__size ** 2)

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print
        for length in range(0, self.__size):
            for width in range(0, self.__size):
                print("#", end="")
            print()
