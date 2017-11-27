#!/usr/bin/python3
"""
sends a request to URL and displays the body
of the response (decoded in utf-8)
prints error code for urllib.error.HTTPError
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            dc = html.decode('utf8')
        print(dc)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
