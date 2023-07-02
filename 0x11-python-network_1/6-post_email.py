#!/usr/bin/python3
'''module:
send POST request to URL with a parameter;
display the body of the response.
'''

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    e_mail = sys.argv[2]

    email = {'email': e_mail}
    body = requests.post(url, data=email)

    print(body.text)
