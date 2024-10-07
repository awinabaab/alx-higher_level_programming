#!/usr/bin/python3
"""The Rectangle class module
"""


class Rectangle:
    """The Rectangle class definition
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle instance initialization

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter for private instance attribute ``width``
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for private instance attribute ``width``

        Args:
            value (int): value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
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
            value (int): value for the height

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
        """Returns the perimeter of the rectangle

        Returns 0 if width or height is 0
        """

        if (self.__width == 0) or (self.__height == 0):
            return (0)

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints the rectangle with print_symbol attribute

         Prints an empty string if width or height is 0
        """

        if (self.__width == 0) or (self.__height == 0):
            return ("")

        return ((('#' * self.__width) + '\n') * self.__height)[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle
        """

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Destructor for Rectangle instance deletion
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
