#!/bin/usr/python3

def element_at(my_list, idx):

    print("length = {}".format(len(my_list)))

    if idx >= len(my_list) - 1:
        return None

    return my_list[idx]
