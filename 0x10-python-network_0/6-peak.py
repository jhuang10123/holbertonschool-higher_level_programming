#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """
def find_peak(list_of_integers):
    for idx, val in enumerate(list_of_integers):
        if list_of_integers[idx + 1] < val and idx != 0:
            if list_of_integers[idx - 1] < val:
                return val
