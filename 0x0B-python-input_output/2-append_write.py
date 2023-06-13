#!/usr/bin/python3

"""Define append_write function"""


def append_write(filename="", text=""):
    """append text to end of file"""
    with open(filename, 'a', encoding='uft-8') as f:
        return f.write(text)
