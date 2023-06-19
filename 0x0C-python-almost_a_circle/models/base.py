#!/usr/bin/python3

"""This module defines the Base class."""

import json


class Base:
    """Base class for managing ID attributes.

    Attributes:
        __nb_objects (int): Counter for generating unique IDs.

    Methods:
        __init__(self, id=None): Constructor method for Base class.
        to_json_string(list_dictionaries): Static method to return the JSON string representation of list_dictionaries.
        save_to_file(cls, list_objs): Class method to write the JSON string representation of list_objs to a file.
        from_json_string(json_string): Static method to return the list represented by json_string.

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
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.

        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
