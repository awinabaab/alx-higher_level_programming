#!/usr/bin/python3
"""Defines a Square class
"""


class Square:
    """Defines a Square class
    """

    def __init__(self, size=0):
        """
        Initializes a Square object

        Args:
            size (int): size of the square(private)
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets self.__size

        Returns: the value of self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of self.__size
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of an instance
        Returns: the area
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks equality based on area
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks inequality based on area
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if this instance greater than another instance based on area
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if this instance is larger or equal to another based on area
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if this instance is less than another based on area
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if this instance is less than of equal to another based on area
        """
        return self.area() <= other.area()
