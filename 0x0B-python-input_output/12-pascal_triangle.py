#!/usr/bin/python3

"""Define function pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n.

    Args:
        n: The number of rows in the Pascal's triangle.

    Returns:
        A list representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []
    else:
        result = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result
