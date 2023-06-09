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

    @classmethod
    def create(cls, **dictionary):
        """
        Return class instantiated for a dictionary
        """
        if dictionary:
            new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Return list of classes from JSON strings file
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                dic = Base.from_json_string(file.read())
                return [cls.create(**d) for d in dic]
        except IOError:
            return []
