#!/usr/bin/python3

"""Define function"""


def class_to_json(obj):
    """Return dictionary"""
    return {key: value for key, value in obj.__dict__.items()
            if type(value) in [list, dict, str, int, bool]}
