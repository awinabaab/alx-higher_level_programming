#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a_cpy = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a_cpy = (tuple_a[0], 0)
    elif len(tuple_a) >= 2:
        tuple_a_cpy = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tuple_b_cpy = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b_cpy = (tuple_b[0], 0)
    elif len(tuple_b) >= 2:
        tuple_b_cpy = (tuple_b[0], tuple_b[1])

    idx_0_result = tuple_a_cpy[0] + tuple_b_cpy[0]
    idx_1_result = tuple_a_cpy[1] + tuple_b_cpy[1]
    result = (idx_0_result, idx_1_result)

    return result
