#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''Deletes keys with a specific value in a dictionary'''

    if value in a_dictionary.values():
        for k in list(a_dictionary.keys()):
            if a_dictionary[k] == value:
                del a_dictionary[k]
    return a_dictionary
