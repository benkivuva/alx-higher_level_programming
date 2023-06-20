#!/usr/bin/python3

"""Defines unittests for models/square.py."""

import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(5)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        self.assertEqual(s.display(), expected_output)

    def test_str(self):
        s = Square(5, 1, 2, 100)
        self.assertEqual(str(s), "[Square] (100) 1/2 - 5")

    def test_update(self):
        s = Square(5)
        s.update(7, 10, 20, 30)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 100)
        expected_dict = {'id': 100, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
