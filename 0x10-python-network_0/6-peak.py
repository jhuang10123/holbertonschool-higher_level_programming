#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    if list_of_integers is None:
        return None
    for idx, val in enumerate(list_of_integers):
        if idx != 0 and idx != len(list_of_integers) - 1:
            if list_of_integers[idx - 1] < val > list_of_integers[idx + 1]:
                return val
