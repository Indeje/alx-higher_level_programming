#!/usr/bin/python3

""" Read file """


def read_file(filename=''):

    """
        Function that reads text file
    """

    with open(filename, encoding='utf8') as newfile:
        for line in newfile:
            print(line, end='')
