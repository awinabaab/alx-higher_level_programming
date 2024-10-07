#!/usr/bin/python3
"""A module that prints a text with 2 new lines after each of these characters:
    ``.``, ``?`` and ``:``
"""


def text_indentation(text):
    """A function that prints new lines after each of these characters:
    ``.``, ``?`` and ``:``

    Args:
        text (str): Text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    idx = 0

    while idx < len(text):
        new_str += text[idx]
        if text[idx] in ('.', '?', ':'):
            new_str += "\n\n"
            idx += 1
            if idx < len(text) and text[idx] == " ":
                idx += 1
            continue
        idx += 1

    print(new_str, end="")
