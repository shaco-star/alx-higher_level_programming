#!/usr/bin/python3

"""Json module"""
import json


def load_from_json_file(filename):
    """Create object from JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.load(f)
