#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Find max - biggest integer of a list'''

    if len(my_list) == 0:
        return None
    return sorted(my_list)[-1]
