#!/usr/bin/python3
def print_last_digit(number):
    '''Return last digit'''

    # absolute value of for negative numbers
    if (number < 0):
        number *= -1

    # last digit
    last_digit = number % 10
 
    print('{}'.format(last_digit), end='')
    return last_digit
