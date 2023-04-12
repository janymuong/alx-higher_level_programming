#!/usr/bin/python3
'''Module:  Write to a file'''


def write_file(filename="", text=""):
    '''
    Write text to the specified file
    and return the number of characters written.
    If the file doesn't exist, create it;
    if it does exist, overwrite its contents.
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
    # f.close()
