#!/usr/bin/python3
"""101-add_attribute.py module
"""


def add_attribute(obj, attribute, value):
    """Adds anew attribute to an object if possible
    """
    if hasattr(obj, '__slots__') or not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
