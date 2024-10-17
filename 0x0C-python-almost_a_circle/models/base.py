#!/usr/bin/python3
"""base.py module
Provides the class definition of Base
"""


class Base:
    """Base class definiton
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate base object with id
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
