#!/usr/bin/python3


def best_score(my_dict):

    while my_dict:
        return sorted(my_dict.keys())[-1]

    return None
