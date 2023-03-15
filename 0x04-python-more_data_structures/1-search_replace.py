#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''replace all occurrences of an element by another in a new list'''

    return [replace if elem == search else elem for elem in my_list]
