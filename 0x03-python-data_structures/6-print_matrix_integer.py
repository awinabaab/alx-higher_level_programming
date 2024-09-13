#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in range(0, len(matrix)):
        mat = matrix[rows]
        for row in range(0, len(mat)):
            print("{:d}".format(mat[row]),
                  end=' ' if row < len(mat) - 1 else '')
        print()
