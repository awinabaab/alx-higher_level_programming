#!/usr/bin/python3
"""12-pascal_triangle.py module
"""


def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle of n
    """
    triangle = []
    for i in range(n):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        if i != 0:
            triangle[i].append(1)
    return (triangle)
