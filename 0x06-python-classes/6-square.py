#!/usr/bin/python3
"""A class that defines a Square
"""


class Square:
    """A class that defines a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Sqaure object

        Args:
            size (int): size of the Square object
            position (tuple): tuple of two integers
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the value of self.__size

        Returns the value of self.__size
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets self.__size to a new value

        Args:
            value (int): new value for self.__size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the value of self.__position

        Returns: the value of self.__position
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets self.__position to a new value

        Args:
            value (int): new value for self.__position

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns: the area of the object
        """

        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #
        """

        if (self.__size == 0):
            print()
            return
        for space in range(0, self.__position[1]):
            print()
        for square in range(0, self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
