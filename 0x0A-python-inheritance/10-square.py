#!/usr/bin/python3
"""10-square.py module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class definition
    """

    def __init__(self, size):
        """Constructor for Square instance initialization

        Args:
            size (int): Size of the square
        """
        super().__init__(size, size)
        self.__size = Rectangle.integer_validator(self, "size", size)

    def area(self):
        """Returns the area of the square
        """
        return (super().area())

    def __str__(self):
        """Returns a string representation of the square
        """
        return (super().__str__())
