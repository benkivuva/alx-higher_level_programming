#!/usr/bin/python3
""" define number_of_lines function """


def write_file(filename="", text=""):
    """function that write a file"""
    with open(filename, "w+", encoding="utf_8") as file:
        return file.write(text)
