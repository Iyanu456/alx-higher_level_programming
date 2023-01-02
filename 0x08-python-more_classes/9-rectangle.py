#!/usr/bin/python3
"""
Rectangle class module.

"""


class Rectangle():
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle."""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets/set the width of a rectangle."""

        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/set the height if a rectangle."""

        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that calculates the area of a rectangle."""

        return (self.__width * self.__height)

    def perimeter(self):
        """Method that calculates the perimeter of a rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle
        based on Area.

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return (rect_1)

        elif rect_1.area() < rect_2.area():
            return (rect_2)

        else:
            return (rect_1)

    def __str__(self):
        """Returns the printaable representation of the Rectangle"""

        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return (rect_str)

        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.width
            if i + 1 < self.__height:
                rect_str += "\n"
        return (rect_str)

    def __repr__(self):
        """Return the string representation of the Rectangle"""

        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Prints a message when the ``del`` method iss called"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
