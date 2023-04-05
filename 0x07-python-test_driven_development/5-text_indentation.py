#!/usr/bin/python3
'''
Module for: function that prints a text with 2 new lines
after each of these characters(delimeters): ., ? and :
'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): the input string
    Raises:
        TypeError: if the input argument is not a string
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    delims = ['.', '?', ':']

    for i in range(len(text)):
        if text[i] not in delims:
            if text[i] == ' ':
                if text[i - 1] in delims:
                    continue
            print('{}'.format(text[i]), end='')
        else:
            print(f'{text[i]}')
            print()
