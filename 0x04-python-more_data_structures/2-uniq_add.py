#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''adds all unique integers in a list (only once for each integer)'''

    tmp_set = set(my_list)
    return sum(tmp_set)
