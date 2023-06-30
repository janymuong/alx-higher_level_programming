#!/usr/bin/python3
'''module:
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
'''
import urllib.request
import sys

url = sys.argv[1]


if __name__ == '__main__':
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        x_request_id = res.headers.get('X-Request-Id')

    print(f'{x_request_id}')