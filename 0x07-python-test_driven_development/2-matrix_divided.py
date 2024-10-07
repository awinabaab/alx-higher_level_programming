#!/usr/bin/python3
"""A module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix

    Args:
        matrix (int)/(float): list of lists of integers/floats
        div (int/float): divisor

    Raises:
        TypeError: if div is neither a float nor an integer
                   if any of the elements in matrix is not a float or an int
                   if any of the lists are not of the same size

        ZeroDivisionError: if div is 0

    Returns: a new matrix with each element divided by div to 2 decimal places
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda row:
                          list(map(lambda num: round(num / div, 2), row)),
                          matrix))
    return new_matrix
