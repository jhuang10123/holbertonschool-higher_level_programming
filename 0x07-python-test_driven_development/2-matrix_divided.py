#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ returns new matrix with each element divided by div """

    new_matrix = []
    list_len = len(matrix[0])

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        temp = []
        if len(row) != list_len:
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if type(i) == int or type(i) == float:
                res = i/div
                i = round(res, 2)
                temp.append(i)
            else:
                raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
        new_matrix.append(temp)

    return new_matrix
