#!/usr/bin/python3

"""
This module defines the Base class.
"""

import csv
import json


class Base:
    """Base class for managing ID attributes.

    Attributes:
        __nb_objects (int): Counter for generating unique IDs.

    Methods:
        __init__(self, id=None): Constructor method for Base class.
        to_json_string(list_dictionaries): Convert list of dict to JSON string.
        save_to_file(cls, list_objs): Save lst of instanc to a file as JSON str
        from_json_string(json_string): Convert JSON str to lst of dictionaries.
        create(cls, **dictionary): Create an instance with ats frm dictionary.
        load_from_file(cls): Load instances from a file.
        save_to_file_csv(cls, list_objs): Save list of instances to a file as a CSV.
        load_from_file_csv(cls): Load instances from a CSV file.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an ID.

        Args:
            id (int, optional): The ID to assign. Defaults to None.

        Note:
            If id is provided, it will be assigned to the instance attribute 'id'.
            If id is not provided, a unique ID will be generated and assigned.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON string representation of the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of instances to a file as a JSON string.

        Args:
            list_objs (list): List of instances to save.

        Note:
            The filename will be <Class name>.json (e.g., Rectangle.json).

        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by the JSON string.

        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary representing attribute names and values.

        Returns:
            Base: An instance with attributes set according to the dictionary.

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            dummy = None

        dummy.update(**dictionary)  # Update the dummy instance with the actual attribute values
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a file.

        Returns:
            list: List of instances loaded from the file.

        Note:
            The filename will be <Class name>.json (e.g., Rectangle.json).

        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**dict_data) for dict_data in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list of instances to a file as a CSV.

        Args:
            list_objs (list): List of instances to save.

        Note:
            The filename will be <Class name>.csv (e.g., Rectangle.csv).
            Format of the CSV: Rectangle: <id>,<width>,<height>,<x>,<y> | Square: <id>,<size>,<x>,<y>.

        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file.

        Returns:
            list: List of instances loaded from the file.

        Note:
            The filename will be <Class name>.csv (e.g., Rectangle.csv).

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                instance_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dict_data = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        dict_data = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                    instance = cls.create(**dict_data)
                    instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []
