#!/usr/bin/python3
'''module:
uses the GitHub API to display your GitHub user ID.
'''

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    git_user = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    res = requests.get(url, auth=HTTPBasicAuth(git_user, password))

    if res.status_code == 200:
        data = res.json()
        print(data['id'])
    else:
        print('None')
