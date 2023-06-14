#!/usr/bin/python3

"""Define Myint Class"""


class MyInt(int):
    """
    MyInt subclass of int that has its == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Overrides the == operator to return the
        result of calling != on the parent class.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to return the
        result of calling == on the parent class.
        """
        return super().__eq__(other)
