#!/usr/bin/python3
def uppercase(s):
    '''print a character string in uppercase followed by a new line'''
    for c in s:
        # 32 - diff(ASCII values of uppercase and lowercase characters)
        if ord(c) >= 97 and ord(c) < 123:
            c = chr(ord(c) - 32)
        print('{}'.format(c), end='')
    print('')
