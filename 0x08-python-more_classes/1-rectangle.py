#!/usr/bin/python3
"""A module that defines a Rectangle class
"""


class Rectangle:
    """A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle instance initialization

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private instance attribute ``width``
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for private instance attribute ``width``

        Args:
            value (int): value for ``width``
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for private instance attribute ``height``
        """

        return (self.__heigth)

    @height.setter
    def height(self, value):
        """Setter for private instance attribute ``height``
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__heigth = value
