#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    used like this as import:
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
    print(ne)
    """
    raise NameError(message)
