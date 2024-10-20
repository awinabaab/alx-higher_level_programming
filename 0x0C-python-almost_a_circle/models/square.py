#!/usr/bin/python3
"""suqare.py module
"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Square class definition
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initiliaze Square instance with size, x, y and id
        """
        super().__init__(size, size, x, y, id)

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
        return (self._Rectangle__height)

    @size.setter
    def size(self, value):
        """Assigns a value to width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance
        """
        dictionary = {
                      "id": self.id,
                      "size": self._Rectangle__height,
                      "x": self._Rectangle__x,
                      "y": self._Rectangle__y
                     }
        return (json.loads(json.dumps(dictionary)))

    def update(self, *args, **kwargs):
        """Assigns attributes to instance
        """
        if (args is not None) and (len(args) > 0):
            for (idx, arg) in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self._Rectangle__height = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
        elif (kwargs is not None) and (len(kwargs) > 0):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self._Rectangle__height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
