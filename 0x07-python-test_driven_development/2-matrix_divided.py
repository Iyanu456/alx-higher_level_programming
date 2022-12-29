#!/usr/bin/python3
"""Defines a matrix division function"""

def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = matrix[:]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round((matrix[i][j] / 3), 2)
    return new_matrix
