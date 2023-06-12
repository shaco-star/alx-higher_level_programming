#!/usr/bin/python3

"""Define class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance.
    """
    return isinstance(obj, a_class)
