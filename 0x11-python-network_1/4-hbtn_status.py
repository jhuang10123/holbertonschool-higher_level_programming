#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    tp = type(req.text)
    print("Body response:")
    print("\t - type: {}".format(tp))
    print("\t - content: {}".format(req.text))
