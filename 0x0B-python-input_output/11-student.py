#!/usr/bin/python3

"""Define Student"""


class Student:
    """
    Defines a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: Optional list of strings. If provided,
            only attribute names contained in this list will be retrieved.

        Returns:
            A dictionary containing all the object's attributes
            that are of a simple data structure.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value
                    in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json: A dictionary where the keys are the public
            attribute names and the values are the values
            of the public attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
