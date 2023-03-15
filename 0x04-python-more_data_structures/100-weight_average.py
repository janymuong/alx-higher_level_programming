#!/usr/bin/python3
def weight_average(my_list=[]):
    '''
    returns the weighted average of all integers
    tuple (<score>, <weight>)
    '''

    if my_list == []:
        return 0

    scores = sum([score * weight for score, weight in my_list])
    weights = sum([weight for score, weight in my_list])

    return scores / weights
