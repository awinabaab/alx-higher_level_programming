#!/usr/bin/python3
"""8-class_to_json.py module
"""


def class_to_json(obj):
    """Returns the dictionary decription with simple data structure
    for JSON serialization of an object
    """
    return (obj.__dict__)
