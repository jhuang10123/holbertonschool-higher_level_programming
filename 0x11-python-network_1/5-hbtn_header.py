#!/usr/bin/python3
"""
takes in a URL, sends a request to the
URL and displays the value of the variable
X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    import sys
    try:
        req = requests.get(sys.argv[1])
        hd = req.headers["X-Request-Id"]
        print(hd)
    except:
        pass
