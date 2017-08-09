#!/usr/bin/python3


def search_replace(my_list, search, replace):
    list = []

    list += [replace if my_list[i] == search else my_list[i] for i in my_list]
    return list
