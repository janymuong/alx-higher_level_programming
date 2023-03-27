#!/usr/bin/python3
def raise_exception():
    """
    Raises a TypeError - exception
    can be used as import in a file like this:
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
    """
    raise TypeError
