#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x * x, nested_list)) for nested_list in matrix]
