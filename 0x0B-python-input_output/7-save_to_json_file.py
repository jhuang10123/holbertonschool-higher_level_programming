#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="UTF8") as file:
        json.dump(my_obj, file)
