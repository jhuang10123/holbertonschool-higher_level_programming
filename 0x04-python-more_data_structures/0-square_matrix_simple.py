#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new = []

    for row in matrix:
        new += ([i**2 for i in row])

    return new
