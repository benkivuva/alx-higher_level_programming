#!/usr/bin/python3

"""
The module is add_interger
It adds two intergers together
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Parameters:
    a (int or float): The first integer or float.
    b (int or float): The second integer or float. Default is 98.

    Returns:
    int: The sum of a and b as an integer.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
