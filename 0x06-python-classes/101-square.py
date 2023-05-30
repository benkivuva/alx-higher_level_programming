#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __str__(self):
        """Returns string representation."""
        return self.my_sprint()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Length of a side of the square.
            position: Position of the square.
        """
        self._size = None
        self._position = None
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the length of a side of this square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    @property
    def position(self):
        """Property for the position of this square."""
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self._position = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.size ** 2

    def my_sprint(self):
        """Returns string representation of this square."""
        ret = ""
        if not self.size:
            return "\n"

        for _ in range(self.position[1]):
            ret += "\n"
        for _ in range(self.size):
            ret += " " * self.position[0] + "#" * self.size + "\n"
        return ret

    def my_print(self):
        """Prints this square."""
        print(self.my_sprint(), end="")
