#!/usr/bin/python3
'''
Module: for Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    list of lists of integers representing the Pascal’s triangle of n
    '''

    if n <= 0:
        return []

    ret_list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(ret_list[i-1][j-1] + ret_list[i-1][j])
        row.append(1)
        ret_list.append(row)

    return ret_list
