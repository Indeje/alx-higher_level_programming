#!/usr/bin/python3

def read_file(filename=''):
    with open(filename, encoding='utf8') as newfile:
        for line in newfile:
            print(line, end='')
