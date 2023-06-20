#!/usr/bin/python3

"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle
    class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the square class.

        Args:
            size (int): Size of the square.
            x (int): Optional integer argument.
            y (int): Optional integer argument.
            id (int): Optional integer argument.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return format of Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @size.setter
    def size(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
