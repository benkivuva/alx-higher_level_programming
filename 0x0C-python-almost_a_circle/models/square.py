#!/usr/bin/python3

"""
This module defines the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square shape.

    Attributes:
        No additional attributes.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a Square instance.

        Properties (getters and setters):
            size
            x
            y
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.

        Note:
            The __init__ method of the Rectangle class is called using super().
            Width and height are set to the value of size.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: String representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
