#!/usr/bin/python3
"""2-append_write.py module
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file(UTF*)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        char_count = f.write(text)
        return (char_count)
