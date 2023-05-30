#!/usr/bin/python3

"""Define Square class"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        self.__size = size

    """Getter for square"""
    @property
    def size(self):
        return self.__size

    """Setter for square"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Get area of square"""
    def area(self):
        return self.__size * self.__size

    """print square with hash #"""
    def my_print(self):
        for x in range(self.__size):
            for row in range(self.__size):
                print("#", end="")
            print('')
        if self.__size == 0:
            print("")
