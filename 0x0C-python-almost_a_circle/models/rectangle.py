#!/usr/bin/python3

"""
This module defines the Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle shape.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): x-coordinate of the rectangle's position.
        __y (int): y-coordinate of the rectangle's position.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a Rectangle instance.

        area(self):
            Returns the area value of the Rectangle instance.

        display(self):
            Prints the Rectangle instance using the character '#'.

        __str__(self):
            Returns a string representation of the Rectangle instance.

        update(self, *args):
            Assigns arguments to each attribute of the Rectangle instance.

        Properties (getters and setters):
            width
            height
            x
            y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-cordinat of rectangle position. Defaults to 0.
            y (int, optional): y-cordinat of rectangle position. Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.

        Note:
            The __init__ method of Base class is called to handle ID assignment
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance using the character '#'.
        Takes care of the position using x and y coordinates.
        """
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args):
        """
        Assign arguments to each attribute of the Rectangle instance.

        Args:
            *args: Arguments in the order: id, width, height, x, y.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

