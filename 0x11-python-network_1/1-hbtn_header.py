#!/usr/bin/python3
"""
sends request and uses 'X-Request-Id'
as key to retrive value from info()
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()

    info = response.info()
    print(info['X-Request-Id'])
