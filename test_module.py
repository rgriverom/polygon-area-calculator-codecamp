"""PyTest Module"""
from unittest import main, TestCase

from shape_calculator import Rectangle, Square


class TestPolygonAreaCalculator(TestCase):
    def setUp(self):
        self.rect = Rectangle(3, 6)
        self.sq = Square(5)

    def test_subclass(self):
        current = issubclass(Square, Rectangle)
        expected = True
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_distinct_classes(self):
        current = Square is not Rectangle
        expected = True
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_square_is_square_and_rectangle(self):
        current = isinstance(self.sq, Square) and isinstance(self.sq, Rectangle)
        expected = True
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_rectangle_string(self):
        current = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_square_string(self):
        current = str(self.sq)
        expected = "Square(side=5)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_area(self):
        current = self.rect.get_area()
        expected = 18
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )
        current = self.sq.get_area()
        expected = 25
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_perimeter(self):
        current = self.rect.get_perimeter()
        expected = 18
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )
        current = self.sq.get_perimeter()
        expected = 20
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_diagonal(self):
        current = self.rect.get_diagonal()
        expected = 6.708203932499369
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )
        current = self.sq.get_diagonal()
        expected = 7.0710678118654755
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_set_attr(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        current = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )
        current = str(self.sq)
        expected = "Square(side=2)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )
        self.sq.set_width(4)
        current = str(self.sq)
        expected = "Square(side=4)"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_rectangle_picture(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        current = self.rect.get_picture()
        expected = "*******\n*******\n*******\n"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_squares_picture(self):
        self.sq.set_side(2)
        current = self.sq.get_picture()
        expected = "**\n**\n"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_big_picture(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        current = self.rect.get_picture()
        expected = "Too big for picture."
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_get_amount_inside(self):
        self.rect.set_height(10)
        self.rect.set_width(15)
        current = self.rect.get_amount_inside(self.sq)
        expected = 6
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_get_amount_inside_two_rectangles(self):
        rect2 = Rectangle(4, 8)
        current = rect2.get_amount_inside(self.rect)
        expected = 1
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_get_amount_inside_none(self):
        rect2 = Rectangle(2, 3)
        current = rect2.get_amount_inside(self.rect)
        expected = 0
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )


if __name__ == "__main__":
    main()
