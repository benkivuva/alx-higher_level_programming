#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Prints the name in formart "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name
        last_name (str): The last name. Defaults to an empty string.


    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("First name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last name must be a string")

    full_name = " ".join(filter(None, [first_name, last_name]))
    print("My name is {}".format(full_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")