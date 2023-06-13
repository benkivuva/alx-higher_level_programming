#!/usr/bin/python3
""" define number_of_lines function """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    line_count = 0
    with open(filename, "r") as file:
        for line in file:
            line_count += 1
    return line_count
