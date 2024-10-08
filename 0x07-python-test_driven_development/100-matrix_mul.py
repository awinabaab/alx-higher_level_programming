#!/usr/bin/python3
"""A module for matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices

    Args:
        m_a (list): list of list of integers floats
        m_b (list): list of list of integers floats

    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        TypeError: if m_a or m_b does not contain only integers/floats
        TypeError: if all rows in m_a or m_b are not of the same size
        ValueError: if m_a or m_b is empty
        ValueError: if m_a and m_b can't be multiplied

    Returns: a new matrix containing the multiplied results
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(mat, list) for mat in m_a):
        raise TypeError("m_a must be a list of list")
    if not all(isinstance(mat, list) for mat in m_b):
        raise TypeError("m_b must be a list of list")
    if all(len(mat) == 0 for mat in m_a):
        raise ValueError("m_a can't be empty")
    if all(len(mat) == 0 for mat in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for mat in m_a for num in mat):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for mat in m_b for num in mat):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(map(len, m_a))) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(map(len, m_b))) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    product = []
    for i in range(len(m_a)):
        product.append([])
        for j in range(len(m_b[0])):
            sum_product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            product[i].append(sum_product)

    return (product)
