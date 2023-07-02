#!/usr/bin/python3
'''module:
sends a POST request to search for a user based on a letter(character) param
and displays the results.
'''

import requests
import sys

msg = ['No result', 'Not a valid JSON']


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    char = sys.argv[1] if len(sys.argv) > 1 else ''

    res = requests.post(url, data={'q': char})

    try:
        data = res.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print(msg[0])
    except ValueError:
        print(msg[1])
