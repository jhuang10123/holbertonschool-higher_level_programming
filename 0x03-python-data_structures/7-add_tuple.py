#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    sumlist = []
    a = list(tuple_a) + [0, 0]
    b = list(tuple_b) + [0, 0]

    for i in range(2):
        sumlist.append(a[i] + b[i])

    return tuple(sumlist)
