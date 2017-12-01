#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the
letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    payload = {'q': q}

    req = requests.post(url, data=payload)

    try:
        req_jsn = req.json()
        if len(req_jsn) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req_jsn.get('id'), req_jsn.get('name')))
    except BaseException:
        print("Not a valid JSON")
