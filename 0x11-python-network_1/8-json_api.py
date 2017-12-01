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
    q=""
    if len(sys.argv) > 1:
        print("pass argv")
        q=sys.argv[1]

    data = {'q':q}

    req = requests.post(url, params=data)

    try:
        req_jsn = req.json()
        if len(req_jsn) == 0:
            print("No result")
        # if req_json == {} or 'name' not in req_json:
        #     print("No result")
        # else:
        #     print("[{}] {}".format(req_jsn['id'],req_jsn['name']))
    except:
            print("Not a valid JSON")



