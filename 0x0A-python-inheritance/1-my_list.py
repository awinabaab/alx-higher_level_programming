#!/usr/bin/python3
"""MyList class module
"""


class MyList(list):
    """MyList class definition
    """

    def print_sorted(self):
        """Prints a list in sorted ascending order
        """
        return (sorted(self))
