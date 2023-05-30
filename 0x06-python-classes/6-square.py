#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __str__(self):
        """String representation of the square."""
        return self.my_sprint()

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size (int): Length of a side of the square.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property for the position of this square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position property."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of this square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_sprint(self):
        """Return string representation of this square."""
        if not self.size:
            return "\n"

        ret = ""
        ret += "\n" * self.position[1]
        for _ in range(self.size):
            ret += " " * self.position[0]
            ret += "#" * self.size
            ret += "\n"
        return ret

    def my_print(self):
        """Print the square."""
        print(self.my_sprint(), end="")
