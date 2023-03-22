#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda nested_list: list(map(lambda x: x * x, nested_list)), matrix))
