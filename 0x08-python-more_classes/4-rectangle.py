#!/usr/bin/python3
"""The Rectangle class module
"""


class Rectangle:
    """The Rectangle class definition
    """

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle instance initialization

        Args:
            width (int): the width of the rectangle
            heigth (int): the height of the rectangle
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

        Raises:
            TypeError: if value is not an integer
            ValueError: if vlaue < 0
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

        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for private instance attribute ``height``

        Args:
            value (int): value for width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """

        self.__height = value

    def area(self):
        """Returns the area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the reactangle
        """

        if (self.__width == 0) or (self.__height == 0):
            return (0)

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns and informal string representation of the rectangle
        """

        if (self.__width == 0) or (self.__height == 0):
            return ("")

        return ((('#' * self.__width) + '\n') * self.__height)[:-1]

    def __repr__(self):
        """Returns a formal string representation of the reactangle
        """

        return ("Rectangle({}, {})".format(self.__width, self.__height))
