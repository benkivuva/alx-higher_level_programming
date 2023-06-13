#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:

    - Prototype: def load_from_json_file(filename):
    - You must use the with statement
    - You donnot need to manage exceptions if the JSON string
    doesnot represent an object.

"""
from json import load


def load_from_json_file(filename):
    """function that that creates an Object from a “JSON file”"""
    with open(filename, encoding="utf_8") as file:
        return load(file)
