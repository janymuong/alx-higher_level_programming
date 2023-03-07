#!/usr/bin/python3
def islower(c):
    '''
    check if a character is lowercase
    comparing its ASCII value with the ASCII values of (a-z).

    Returns True if c is lowercase, else False.
    '''
    
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
