#!/usr/bin/python3
"""100-my_int.py module
"""


class MyInt(int):
    """MyInt clas definition
    """
    def __init__(self, value):
        """Constructor for MyInt instances
        """
        self.__value = value
        super().__init__()

    def __eq__(self, other):
        """Returns the inverse of the equality operator
        """
        return (not (self.__value == other))

    def __ne__(self, other):
        """Returns the inverse of the inequality operator
        """
        return (self.__value == other)
