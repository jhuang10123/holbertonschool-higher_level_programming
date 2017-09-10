#!/usr/bin/python3
def class_to_json(obj):
    """returns the dict description w/ simple data structure"""
    return obj.__dict__
