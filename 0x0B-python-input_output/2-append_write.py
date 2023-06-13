#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:

    - Prototype: def append_write(filename="", text=""):
    - If the file doesnot exist, it should be created
    - You must use the with statement
    - You donot need to manage file permission or file doesn't exist
    exceptions.

"""


def append_write(filename="", text=""):
    """function that write a file"""
    with open(filename, "a", encoding="utf_8") as file:
        return file.write(text)
