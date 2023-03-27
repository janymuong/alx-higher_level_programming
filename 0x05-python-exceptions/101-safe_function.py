#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    '''executes a function safely'''

    try:
        result = fct(*args)
        return result
    except Exception as exc:
        sys.stderr.write(f"Exception: {exc}\n")
        return None
