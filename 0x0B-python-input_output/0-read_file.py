#!/usr/bin/python3
"""0-read_file.py module
"""


def read_file(filename=""):
    """Reads a tet file(UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
