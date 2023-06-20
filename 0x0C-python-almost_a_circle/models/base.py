#!/usr/bin/python3

"""Define Base class"""
import json


class Base:
    """
    Base class for all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): Optional integer argument.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert dictionary to json format
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert from json to string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json converted string to file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dic = [x.to_dictionary() for x in list_objs]
                file.write(Base.to_json_string(dic))
