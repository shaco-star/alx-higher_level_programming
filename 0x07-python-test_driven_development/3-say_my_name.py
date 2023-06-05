#!/usr/bin/python3

"""This is 3-say_my_name module"""


def say_my_name(first_name, last_name=""):
    """say_my_name function
    Args:
        first_name (str) : first name of user
        last_name (str) : last name of user

    Raise:
        TypeError : first and last name must be string only

    Return:
        String sentence contain first and last
        name of user
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return print("My name is {} {}".format(first_name, last_name))
