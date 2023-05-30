#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represent  a new square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): The size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
