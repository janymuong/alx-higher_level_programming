#!/usr/bin/python3
def remove_char_at(string, n):
    '''
    creates a copy of the string, removing the character at the position n
    emulates C array indexing
    '''
    if n < 0 or n >= len(string):
        return string
    else:
        return string[:n] + string[n+1:]
