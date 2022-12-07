#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for i in range(len(new_matrix)):
        for k in range(len(matrix[i])):
            new_matrix[i][k] = matrix[i][k]**2
    return (new_matrix)
