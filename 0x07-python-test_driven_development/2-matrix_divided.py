#!/usr/bin/python3


"""This is matrix_divided module"""


def matrix_divided(matrix, div):
    """ Function that divide matrix
    Args:
        matrix : the matrix
        div : number that will be used to divide matrix
    Return:
        matrix after divition
    """
    if not isinstance(matrix, list) or
    not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
