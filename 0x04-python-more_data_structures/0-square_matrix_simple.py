#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = [i**2 for x in row]
        new_matrix.appned(row)
    return new_matrix
