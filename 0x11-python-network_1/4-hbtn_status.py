#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    tp = req.text
    print("Body response:")
    print("\t- type: {}".format(type(tp)))
    print("\t- content: {}".format(tp))
