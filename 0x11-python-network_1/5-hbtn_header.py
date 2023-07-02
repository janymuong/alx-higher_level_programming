#!/usr/bin/python3
'''module:
sends a request to a URL;
displays the value of the variable `X-Request-Id` in the response header
'''

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    res = requests.get(url)
    x_request_id = res.headers.get('X-Request-Id')

    print(f'{x_request_id}')
