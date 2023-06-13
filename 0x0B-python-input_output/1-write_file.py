#!/usr/bin/python3


"""Define write_file function that read file"""


def write_file(filename="", text=""):
    """print the content of file
    Args
        filename : file that will read
        text : string of text
    Return
        File after appending text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
