#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for idx in range(0, len(matrix)):
            square = list(map(lambda num: num ** 2, matrix[idx]))
            new_matrix.append(square)
        return (new_matrix)
