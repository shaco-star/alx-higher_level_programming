#!/usr/bin/python3

"""Define function to add new attribute"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    :param obj: The object to add the attribute to.
    :param name: The name of the attribute to add.
    :param value: The value of the attribute to add.
    :raises TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
