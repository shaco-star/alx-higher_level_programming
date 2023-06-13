#!/usr/bin/python3

"""Json module"""
import json


def from_json_string(my_str):
    """Function convert json object to python object"""
    return json.loads(my_str)
