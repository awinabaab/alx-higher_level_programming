#!/usr/bin/python3
"""4-from_json_string.py module
"""
import json


def from_json_string(my_obj):
    """Returns an object represented by a JSON string
    """
    return (json.loads(my_obj))
