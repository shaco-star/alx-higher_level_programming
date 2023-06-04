#!/usr/bin/python3


"""" "0-add_integer" module """


def add_integer(a, b=98):
    """" Add 2 numbers together

    Args:
        a (int) : first number
        b (int) : second number

    Return addition of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
