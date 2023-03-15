#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''new dictionary with all values multiplied by 2'''

    dict_2X = {k: val * 2 for k, val in a_dictionary.items()}
    return dict_2X
