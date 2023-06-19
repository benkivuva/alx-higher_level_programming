import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(5, 10)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        self.assertEqual(r.display(), expected_output)

    def test_str(self):
        r = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(str(r), "[Rectangle] (100) 1/2 - 5/10")

    def test_update(self):
        r = Rectangle(5, 10)
        r.update(7, 20, 30, 40, 50)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 1, 2, 100)
        expected_dict = {'id': 100, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
