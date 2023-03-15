#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''prints a dictionary by ordered keys'''

    keys = sorted(a_dictionary)
    for k in keys:
        print(f'{k}: {a_dictionary[k]}')
