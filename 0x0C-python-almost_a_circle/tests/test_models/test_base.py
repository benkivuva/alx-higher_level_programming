#!/usr/bin/python3

"""
This module contains test cases for the Base class.
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_create_rectangle(self):
        """Test the create method for creating a Rectangle instance."""
        dictionary = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rectangle = Rectangle.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_create_square(self):
        """Test the create method for creating a Square instance."""
        dictionary = {'id': 2, 'size': 7, 'x': 1, 'y': 2}
        square = Square.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_save_to_file(self):
        """Test the save_to_file method for saving instances to a file as JSON."""
        rectangle1 = Rectangle(10, 5)
        rectangle2 = Rectangle(7, 3)
        filename = "Rectangle.json"
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open(filename, mode='r', encoding='utf-8') as file:
            json_str = file.read()
            dictionary_list = json.loads(json_str)
            self.assertIsInstance(dictionary_list, list)
            self.assertEqual(len(dictionary_list), 2)
            self.assertEqual(dictionary_list[0]['id'], rectangle1.id)
            self.assertEqual(dictionary_list[0]['width'], rectangle1.width)
            self.assertEqual(dictionary_list[0]['height'], rectangle1.height)
            self.assertEqual(dictionary_list[1]['id'], rectangle2.id)
            self.assertEqual(dictionary_list[1]['width'], rectangle2.width)
            self.assertEqual(dictionary_list[1]['height'], rectangle2.height)

    def test_load_from_file(self):
        """Test the load_from_file method for loading instances from a JSON file."""
        rectangle1 = Rectangle(10, 5)
        rectangle2 = Rectangle(7, 3)
        filename = "Rectangle.json"
        Rectangle.save_to_file([rectangle1, rectangle2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertEqual(loaded_rectangles[0].id, rectangle1.id)
        self.assertEqual(loaded_rectangles[0].width, rectangle1.width)
        self.assertEqual(loaded_rectangles[0].height, rectangle1.height)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[1].id, rectangle2.id)
        self.assertEqual(loaded_rectangles[1].width, rectangle2.width)
        self.assertEqual(loaded_rectangles[1].height, rectangle2.height)

    def test_save_to_file_csv(self):
        """Test the save_to_file_csv method for saving instances to a CSV file."""
        square1 = Square(5)
        square2 = Square(3)
        filename = "Square.csv"
        Square.save_to_file_csv([square1, square2])
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0].strip(), f"{square1.id},{square1.size},{square1.x},{square1.y}")
            self.assertEqual(lines[1].strip(), f"{square2.id},{square2.size},{square2.x},{square2.y}")

    def test_load_from_file_csv(self):
        """Test the load_from_file_csv method for loading instances from a CSV file."""
        square1 = Square(5)
        square2 = Square(3)
        filename = "Square.csv"
        Square.save_to_file_csv([square1, square2])
        loaded_squares = Square.load_from_file_csv()
        self.assertIsInstance(loaded_squares, list)
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertEqual(loaded_squares[0].id, square1.id)
        self.assertEqual(loaded_squares[0].size, square1.size)
        self.assertEqual(loaded_squares[0].x, square1.x)
        self.assertEqual(loaded_squares[0].y, square1.y)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[1].id, square2.id)
        self.assertEqual(loaded_squares[1].size, square2.size)
        self.assertEqual(loaded_squares[1].x, square2.x)
        self.assertEqual(loaded_squares[1].y, square2.y)


if __name__ == "__main__":
    unittest.main()
