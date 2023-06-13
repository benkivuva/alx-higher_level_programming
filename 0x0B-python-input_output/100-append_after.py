#!/usr/bin/python3
"""Insert a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a new string"""

    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as file2:
        i = ""
        for line in text:
            i += line
            if search_string in line:
                i += new_string
        file2.write(i)
