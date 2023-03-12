#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Check for multiples of 2'''

    return [True if i % 2 == 0 else False for i in my_list]
