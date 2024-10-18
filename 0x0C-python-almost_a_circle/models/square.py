#!/usr/bin/python3
"""suqare.py module
"""
from .rectangle import Rectangle
import json


class Square(Rectangle):
    """Square class definition
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initiliaze Square instance with size, x, y and id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of the Square instance
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self._Rectangle__x, self._Rectangle__y,
                self._Rectangle__height))

    @property
    def size(self):
        """Retrieves the value of width
        """
        return (self._Rectangle__width)

    @size.setter
    def size(self, value):
        """Assigns a value to width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self._Rectangle__width = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance
        """
        return (json.loads(json.dumps(self.__dict__)))
