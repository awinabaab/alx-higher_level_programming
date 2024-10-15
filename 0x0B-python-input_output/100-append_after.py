#!/usr/bin/python3
"""100-append_after.py module
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+", encoding="utf-8") as f:
        content = f.readlines()
        lines = []
        for line in content:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        f.truncate(0)
        f.writelines(lines)
