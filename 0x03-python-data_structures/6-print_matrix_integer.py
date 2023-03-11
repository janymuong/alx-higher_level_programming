#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''Print matrix of integers'''

    for row in matrix:
        for elem_pos in range(len(row)):
            if elem_pos == len(row) - 1:
                print('{:d}'.format(row[elem_pos]), end='')
            else:
                print('{:d} '.format(row[elem_pos]), end='')
        print('')
