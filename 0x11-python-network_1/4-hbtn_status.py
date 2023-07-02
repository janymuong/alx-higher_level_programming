#!/usr/bin/python3
'''module:
fetches the status from URL
'''
import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    res = requests.get(url)
    body = res.text

    print(f'Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
