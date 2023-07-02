#!/usr/bin/python3
'''module:
sned a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
'''

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    e_mail = sys.argv[2]

    data = urllib.parse.urlencode({'email': e_mail}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
