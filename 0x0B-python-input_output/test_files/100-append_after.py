#!/usr/bin/python3
'''
Module: search and update
'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file,
    after each line containing a specific string
    '''

    lines = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as f:
        f.writelines(lines)
