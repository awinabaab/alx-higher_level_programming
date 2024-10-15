#!/usr/bin/python3
"""1-write_file.py module
"""


def write_file(filename="", text=""):
    """Writes a string to a text file(UTF*) and
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        char_count = f.write(text)
    return (char_count)
