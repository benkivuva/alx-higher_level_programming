#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    result = ""
    previous_char = ""

    for char in text:
        result += char

        if previous_char in punctuation_marks:
            if char != " ":
                result += "\n\n"

        previous_char = char

    print(result)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")