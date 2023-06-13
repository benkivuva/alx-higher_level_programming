#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, using a
JSON representation:

    - Prototype: def save_to_json_file(my_obj, filename):
    - You must use the with statement
    - You donnot need to manage exceptions if the object cannot be
    serialized.

"""
from json import dump


def save_to_json_file(my_obj, filename):
    """function that return an object to a text file
    Using JSON representation"""
    with open(filename, "w+", encoding="utf_8") as file:
        return dump(my_obj, file)
