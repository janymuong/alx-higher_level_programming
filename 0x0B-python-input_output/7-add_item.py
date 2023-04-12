#!/usr/bin/python3
'''
script that adds all arguments to a Python list,
and then save them to a file:
'''

import sys
from os import path
from typing import List
from json import dump, load

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename: str, item_list: List[str]) -> None:
    '''
    adds all args to a Python list and saves it to a file as JSON
    '''

    if not path.exists(filename):
        save_to_json_file([], filename)

    save_list = load_from_json_file(filename)
    save_list.extend(item_list)
    save_to_json_file(save_list, filename)


if __name__ == '__main__':
    filename = 'add_item.json'
    save_list = sys.argv[1:]
    add_item(filename, save_list)
