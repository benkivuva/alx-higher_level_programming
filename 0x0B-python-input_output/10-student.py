#!/usr/bin/python3
"""
Write a class Student that defines a student by:

    - Public instance attributes:
        - first_name
        - last_name
        - age
    - Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    - Public method def to_json(self, attrs=None): that
    retrieves a dictionary representation of a Student
    instance (same as 8-class_to_json.py):

        - If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved

"""


class Student():
    """class student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
