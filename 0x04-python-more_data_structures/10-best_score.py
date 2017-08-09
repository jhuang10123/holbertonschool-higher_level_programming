#!/usr/bin/python3


def best_score(my_dict):

    while my_dict:
        return sorted(my_dict.keys())[-1]

    return None


"""
    if len(my_dict.keys()) == 0:
        return None

    return sorted(my_dict.keys())[-1]

    sorted(my_dict)

    return my_dict.keys()[-1]
"""
