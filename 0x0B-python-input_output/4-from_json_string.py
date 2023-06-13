#!/usr/bin/python3
"""
Write a function that returns an object (Python data structure)
represented by a JSON string:

    Prototype: def from_json_string(my_str):
    You donnot need to manage exceptions if the JSON string doesnnot
    represent an object.

"""
from json import loads


def from_json_string(my_str):
    """function that return an object represented by a JSON string"""
    return loads(my_str)
