#!/usr/bin/python3

"""4-print_square Module"""


def print_square(size):
    """print_square function print sqaure

    Args:
        size (int) : positive integer size of square
    Raise:
        TypeError : if size is not integer
        ValueError : if size is negative

    Return:
        square made  with # hash
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for x in range(size):
            for row in range(size):
                print("#", end="")
            print('')
        if size == 0:
            print("")
