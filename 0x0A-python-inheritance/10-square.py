#!/usr/bin/python3

"""define class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """init
        args:
            size : size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of Square"""
        return self.__size ** 2
