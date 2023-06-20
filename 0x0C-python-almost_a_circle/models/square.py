#!/usr/bin/python3

from main import Rectangle

"""Define square class"""


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
        :return:
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
