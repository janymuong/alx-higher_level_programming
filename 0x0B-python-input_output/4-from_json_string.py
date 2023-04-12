#!/usr/bin/python3
'''Module: JSON.loads()'''

import json


def from_json_string(my_str):
    '''
    object (Python data structure) represented by a JSON string
    initially JSON representation of an object (string)
    '''
    return json.loads(my_str)
