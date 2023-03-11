#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Modify copy of a list at [index]'''

    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = [x for x in my_list]
    new_list[idx] = element
    return new_list
