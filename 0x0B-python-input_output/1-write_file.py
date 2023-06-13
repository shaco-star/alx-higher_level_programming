#!/usr/bin/python3


"""Define read_file function that read file"""


def read_file(filename="", text=""):
    """print the content of file"""
    with open(filename, 'w', encoding="uft-8") as f:
        return f.write(text)
