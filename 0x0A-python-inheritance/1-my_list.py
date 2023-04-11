#!/usr/bin/python3
'''
Module for:file
class MyList that inherits frm the list class
'''


class MyList(list):
    '''Class'''
    def print_sorted(self):
        '''prints the list, sorted (ascending sort)'''

        print(sorted(self))
