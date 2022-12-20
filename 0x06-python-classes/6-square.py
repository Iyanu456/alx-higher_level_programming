#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, positiion=(0, 0)):
        """Initialize a new square.
        Args:
            size(int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square"""

        return (self.__size * self.__size)

    @property
    def position(self):
        """Gets/sets the current position of the square"""

        return (self.__posiition)

    msg = "position must be a tuple of 2 positive integers"

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError(msg)
        self.__position = value

    def my_print(self):
        """Prints a square"""

        if self.__size == 0:
            print("")
            return

        [print("") for m in range(0, self.__position[1])]
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
