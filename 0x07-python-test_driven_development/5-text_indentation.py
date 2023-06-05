#!/usr/bin/python3

"""5-text_indentation module"""


def text_indentation(text):
    """text_indentation function
    create new line if [.,:,?] incountered

    Args:
        text (str) : string to perform function on it

    Raise:
        TypeError : if @text contains integer

    Return:
        each line of text after indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines = text.split("\n")
    for line in lines:
        print(line.strip())
