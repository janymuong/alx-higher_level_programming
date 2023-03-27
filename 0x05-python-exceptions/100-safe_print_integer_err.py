#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''
    function that prints an integer
    prints to sderr for exceptions as well
    '''

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
