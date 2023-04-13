#!/usr/bin/python3

""" Append text to a file """


def append_write(filename="", text=""):

    """
        Append text to a file
    """

    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
