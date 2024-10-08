#!/usr/bin/python3
"""A Locked class module
"""


class LockedClass:
    """The LockedClass definition
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Constructor for LockedClass instance initialization
        """

        self.first_name = None
