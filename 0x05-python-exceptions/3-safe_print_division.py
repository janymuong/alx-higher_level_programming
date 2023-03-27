#!/usr/bin/python3
def safe_print_division(a, b):
    '''divide two integers and prints the result'''

    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print('Inside result: {}'.format(quotient))
    return quotient
