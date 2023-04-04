#!/usr/bin/python3
def matrix_divided(matrix, div):
    r_size = None
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg)
    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)
        for j in i:
            if not isinstance(j, float):
                raise TypeError(msg)
        if r_size is None:
            r_size = len(i)
        elif r_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
    if not isintance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [[round(j / div, 2) for j in i] for i in matrix]
    return new
