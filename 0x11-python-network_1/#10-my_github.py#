#!/usr/bin/python3
"""
takes Github credentials and uses the
Github API to display id
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pswrd = sys.argv[2]

    req = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(
            usr,
            pswrd))

#    if req.json() is not None:
print(req.json().get('id'))
