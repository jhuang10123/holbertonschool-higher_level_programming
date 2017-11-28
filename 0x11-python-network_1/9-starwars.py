#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""

import requests
import sys

if __name__ == "__main__":
    payload = {'search': sys.argv[1]}
    req = requests.get('https://swapi.co/api/people/', params=payload)
    num = req.json()['count']
    ppl = req.json()['results']
    print("Number of results: {}".format(num))
    for person in ppl:
        print(person['name'])
