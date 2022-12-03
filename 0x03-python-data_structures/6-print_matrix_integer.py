#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for i in range(0, len(row)):
                if i == (len(row) - 1):
                    print("{:d}".format(row[i]))
                elif len(row) <= 0:
                    print()
                    break
                else:
                    print("{:d}".format(row[i]), end=' ')
