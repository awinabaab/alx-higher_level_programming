#!/usr/bin/python3
"""
Defines a magic class
"""
import math


class MagicClass:
    """
    Defines a magic class
    """

    def __init__(self, radius=0):
        """
        Initializes and instance

        Raises:
            TypeError: if radius is not a number
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of a circle
        """
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """
        Calculates the circumference of the circle
        """
        return (2 * math.pi * self.__radius)
