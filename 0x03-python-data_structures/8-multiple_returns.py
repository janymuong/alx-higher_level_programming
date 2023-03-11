#!/usr/bin/python3
def multiple_returns(sentence):
    '''
    Returns a tuple with the length of a string
    and its first character.
    '''

    len_str = len(sentence)
    if len_str == 0:
        first_char = None

    first_char = sentence[0]
    return (len_str, first_char)
