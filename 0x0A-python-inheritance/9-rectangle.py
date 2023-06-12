#!/usr/bin/python3


"""Define class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            """Area"""
            return self.__width * self.__height

        def __str__(self):
            """str"""
            return f"[Rectangle] {self.__width}/{self.__height}
