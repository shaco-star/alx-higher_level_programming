#!/usr/bin/python3

"""Json module"""
import json


def save_to_json_file(my_obj, filename):
    """Write json object to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
