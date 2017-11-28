#!/usr/bin/python3
"""
takes in a letter and sends a POST request to 
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/"
    if sys.argv[1] is None:
        q = ""
    else:
        q = sys.argv[1]
    param = {'search_user':q}
    req = requests.post(url, params=param)
    print (req)
