#!/usr/bin/python3

""" Write to file """


def write_file(filename="", text=""):

    """
        Write text to a file
    """

    with open(filename, mode="w", encoding='utf8') as myfile:
        return myfile.write(text)
