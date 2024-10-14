#!/usr/bin/python3
"""6-base_geometry.py module
"""


class BaseGeometry:
    """Base Geomtry class definition
    """

    def area(self):
        """Raises an exception with the message "area() is not implemented"
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer

        Args:
            name (String): name
            value (int): value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))

        return (value)
