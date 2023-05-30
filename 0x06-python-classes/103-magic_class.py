#!/usr/bin/python3

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area for MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return The circumference for MagicClass."""
        return 2 * math.pi * self.__radius
