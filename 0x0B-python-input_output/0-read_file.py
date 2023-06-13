#!/usr/bin/python3

"""Define read_file function that read file"""


def read_file(filename=""):
    """print the content of file"""
    with open(filename, encoding='uft-8') as f:
        print(f.read(), end='')
