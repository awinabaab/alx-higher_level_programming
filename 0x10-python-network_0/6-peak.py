#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in alist of unsorted integers

    Args:
        list_of_integers: unsorted list of integers
    """

    integers = list_of_integers
    length = len(integers)

    if not integers or length == 0:
        return None

    if length == 1:
        return integers[0]

    right = length - 1
    left = 0

    while left < right:
        mid = (left + right) // 2
        if integers[mid] < integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return integers[left]
