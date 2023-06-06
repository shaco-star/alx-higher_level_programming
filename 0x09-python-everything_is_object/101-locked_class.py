#!/usr/bin/python3

"""Define LockedClass"""


class LockedClass:
    """__slots__ prevent user from creating new LockedClass
    attributes unless its called first_name
    """
    __slots__ = ['first_name']

    def __init__(self):
        pass
