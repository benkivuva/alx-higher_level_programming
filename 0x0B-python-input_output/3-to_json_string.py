#!/usr/bin/python3

from json import dumps


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    :param my_obj: The object to be serialized to JSON.
    :return: The JSON representation of the object.
    """
    return dumps(my_obj)
