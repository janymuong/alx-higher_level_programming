#!/usr/bin/python3
'''Module: Read file'''


def read_file(filename=""):
    '''Read file with a context manager'''

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
