#!/usr/bin/python3

"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix by div.

    Args:
        matrix (list): List of lists containing int or float.
        div (int or float): Number to divide matrix by.

    Returns:
        list: List of lists representing divided matrix.

    Raises:
        TypeError: If matrix is not a list of lists containing int or float.
        TypeError: If sublists are not all the same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a (list of lists) of int/flt")

    row_size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be (list of lists) of int/floats")
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be (list of lists) of int/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
