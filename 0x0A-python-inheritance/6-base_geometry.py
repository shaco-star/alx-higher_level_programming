#!/usr/bin/python3


"""Define class"""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Calculates the area of the geometry.
        """
        raise Exception("area() is not implemented")
