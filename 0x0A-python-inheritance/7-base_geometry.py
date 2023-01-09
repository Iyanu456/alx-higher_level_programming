#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """class BaseGeometry"""

    def integer_validator(self, name, value):
        """Validates if value is an integer greater than 0"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """area not implemented"""

        raise Exception("area() is not implemented")
