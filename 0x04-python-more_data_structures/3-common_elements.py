#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''returns a set of common elements in two sets - intersection'''

    # [x for x in set_1 if x in set_2]
    return set_1 & set_2
