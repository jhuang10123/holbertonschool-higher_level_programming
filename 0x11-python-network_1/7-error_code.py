#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response
HTTP status code is greater than or equal to 400,
print error code
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
