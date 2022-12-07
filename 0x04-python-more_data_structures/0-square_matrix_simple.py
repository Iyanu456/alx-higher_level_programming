#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = []
    for i in matrix:
        tmp.append(list(map(lambda x: x**2, i)))
    return (tmp)
