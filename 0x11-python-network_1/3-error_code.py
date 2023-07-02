#!/usr/bin/python3
'''module:
send a request to a URL and displays the body of the response
else print error code
'''

import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url=url)

    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
