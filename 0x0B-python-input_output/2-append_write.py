#!/usr/bin/python3
'''Module: append text to a file in'''


def append_write(filename="", text=""):
    '''
    append text to the file
    and return the number of characters added.
    If the file doesn't exist, create it.

    args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    '''

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
        # f.close()
