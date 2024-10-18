#!/usr/bin/python3
"""rectangle.py module
Provides the class structure for Rectangle
"""
from .base import Base
import json


class Rectangle(Base):
    """Defines the rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialiazes rectangle object with height, width, x, y and is
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the value of width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Assigns a value to width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Assigns a value to height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the value of x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """Assigns a value to x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """Assigns a value to y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """Prints the Rectangle to stdout with the character #
        """
        print('\n' * self.__y + ((((" " * self.__x) +
              '#' * self.__width) + '\n') * self.__height)[:-1])

    def __str__(self):
        """Returns a string representation of the Rectangle instance
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.__x, self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance
        """
        return (json.loads(json.dumps(self.__dict__)))
