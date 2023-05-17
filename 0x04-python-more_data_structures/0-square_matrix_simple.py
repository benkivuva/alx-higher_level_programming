#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Check if the matrix is not None
    if matrix is not None: 
        result = [list(map(lambda e: e * e, row)) for row in matrix]
        return result
