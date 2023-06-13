#!/usr/bin/python3
"""
Write a function that returns the JSON representation
of an object (string):

    - Prototype: def to_json_string(my_obj):
    - You donnot need to manage exceptions if the object
    cannot be serialized.
"""
from json import dumps


def to_json_string(my_obj):
    """function that return the JSON representation
    of an object"""
    return dumps(my_obj)
