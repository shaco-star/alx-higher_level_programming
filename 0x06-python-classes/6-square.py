#!/usr/bin/python3

"""Define Square class"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """Getter for position"""
    @property
    def position(self):
        return self.__position
    """set position"""
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2
        or not all(isintance(num, int) for num in value) or
        not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    """print square with hash #"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
