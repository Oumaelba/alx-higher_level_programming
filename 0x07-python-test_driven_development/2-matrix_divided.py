#!/usr/bin/python3
"""
    Divide all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """"

    Arguments:
    - matrix: A list of lists representing the matrix.
    - div: The number to divide each element of the matrix by.

    Returns:
    - A new matrix with the elements divided by
    the given number.

    Raises:
    - TypeError: If the matrix is not a list of
    lists or if div is not a number.
    - ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or \
            any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
