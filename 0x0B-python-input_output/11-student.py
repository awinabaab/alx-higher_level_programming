#!/usr/bin/python3
"""11-student module
"""


class Student:
    """Defines a student class
    """

    def __init__(self, first_name, last_name, age):
        """Constructor for Student instantion

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student object
        if attrs is a valid a list of attributes
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return ({k: v for (k, v) in self.__dict__.items() if k in attrs})

        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all the attributes of the Student instance with @json
        """
        self.__dict__ = json
