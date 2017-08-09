#!/usr/bin/python3


def multiply_by_2(my_dict):
    new = my_dict

    for key in new:
        new[key] *= 2

    return new
