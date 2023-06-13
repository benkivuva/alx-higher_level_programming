#!/usr/bin/python3
"""
Technical interview preparation:

    - You are not allowed to google anything
    - Whiteboard first

Create a function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascals triangle of n:

    - Returns an empty list if n <= 0
    - You can assume n will be always an integer

"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
       Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        tri = pascal[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal
