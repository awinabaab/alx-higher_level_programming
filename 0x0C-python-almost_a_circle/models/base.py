#!/usr/bin/python3
"""base.py module
Provides the class definition of Base
"""
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        """
        dictionaries = list()
        if (type(list_dictionaries) is None) or (len(list_dictionaries) < 1):
            return ("[]")
        for dictionary in list_dictionaries:
            dictionaries.append(dictionary)
        return (json.dumps(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        """
        if (type(json_string) is None) or (len(json_string) < 1):
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file
        """

        filename = "{}.json".format(cls.__name__)
        objs = [obj.__dict__ for obj in list_objs]

        with open(filename, "w", encoding="utf-8") as f:
            if type(list_objs) is None:
                f.write(list())
            f.writelines(cls.to_json_string(objs))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        instances = list()
        contents = list()

        with open(filename, "r", encoding="utf-8") as f:
            try:
                contents = f.read()
                instances = cls.from_json_string(contents)
                return (instances)
            except FileNotFoundError:
                return (instances)
