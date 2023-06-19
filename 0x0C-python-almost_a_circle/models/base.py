#!/usr/bin/python3

"""This module defines the Base class."""


class Base:
    """Base class for managing ID attributes.

    Attributes:
        __nb_objects (int): Counter for generating unique IDs.

    Methods:
        __init__(self, id=None): Constructor method for Base class.
        to_json_string(list_dictionaries): Static method to convert list of dictionaries to JSON string.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an ID.

        Args:
            id (int, optional): The ID to assign. Defaults to None.

        Note:
            If id is provided it will be assigned to the instance attribute 'id'.
            If id is not provided, a unique ID will be generated and assigned.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.

        """
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
