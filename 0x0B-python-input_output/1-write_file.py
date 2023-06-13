#!/usr/bin/python3


"""Define read_file function that read file"""


def read_file(filename="", text=""):
    """print the content of file
    Args
        filename : file that will read
        text : string of text
    Return
        File after appending text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
