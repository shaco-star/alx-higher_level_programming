#!/usr/bin/python3


"""Define class"""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")
