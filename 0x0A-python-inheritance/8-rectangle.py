#!/usr/bin/python3
"""8-rectangle.py module
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition
    """

    def __init__(self, width, height):
        """Constructor for instance initialization

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)
