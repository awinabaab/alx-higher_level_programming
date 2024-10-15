#!/usr/bin/python3
"""9-student module
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

    def to_json(self):
        """Retrieve a dictionary representation of a Student object
        """

        return (self.__dict__)
