#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
from unittest.mock import patch
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """A class to test Base class instances
    """

    def setUp(self):
        """Setups an instance
        """
        self.square_all_args = Square(1, 2, 3, 4)
        self.square_one_args = Square(1)
        self.square_two_args = Square(1, 2)
        self.square_three_args = Square(1, 2, 3)

    def tearDown(self):
        """Deletes an instance
        """
        del self

    def test_square_no_arg(self):
        """Test initialization with no args
        """
        with self.assertRaises(TypeError):
            Square()

    def test_square_one_arg(self):
        """Test initialization with one arg @size
        """
        self.assertEqual(self.square_one_args.id, self.square_one_args.id)
        self.assertEqual(self.square_one_args.size, 1)
        self.assertEqual(self.square_one_args.x, 0)
        self.assertEqual(self.square_one_args.y, 0)

    def test_square_two_args(self):
        """Test initialization with two args @size and @x
        """
        self.assertEqual(self.square_two_args.id, self.square_two_args.id)
        self.assertEqual(self.square_two_args.size, 1)
        self.assertEqual(self.square_two_args.x, 2)
        self.assertEqual(self.square_two_args.y, 0)

    def test_square_three_args(self):
        """Test initialization with three args @size, @x and @y
        """
        self.assertEqual(self.square_three_args.id, self.square_three_args.id)
        self.assertEqual(self.square_three_args.size, 1)
        self.assertEqual(self.square_three_args.x, 2)
        self.assertEqual(self.square_three_args.y, 3)

    def test_square_all_args(self):
        """Test initialization with all args @size, @x, @y and @id
        """
        self.assertEqual(self.square_all_args.id, 4)
        self.assertEqual(self.square_all_args.size, 1)
        self.assertEqual(self.square_all_args.x, 2)
        self.assertEqual(self.square_all_args.y, 3)

    def test_square_size_setter(self):
        """Test instance attribute size setter
        """
        with self.assertRaises(TypeError):
            Square("a")

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(TypeError):
            Square(10.5)

        with self.assertRaises(TypeError):
            Square(True)

        with self.assertRaises(TypeError):
            Square(False)

    def test_square_x_setter(self):
        """Test instance attribute x setter
        """
        with self.assertRaises(TypeError):
            Square(10, "x")

        with self.assertRaises(ValueError):
            Square(10, -1)

        with self.assertRaises(TypeError):
            Square(10, 1.5)

        with self.assertRaises(TypeError):
            Square(10, True)

        with self.assertRaises(TypeError):
            Square(10, False)

    def test_square_y_setter(self):
        """Test instance attribute y setter
        """
        with self.assertRaises(TypeError):
            Square(10, 10, "y")

        with self.assertRaises(ValueError):
            Square(10, 10, -1)

        with self.assertRaises(TypeError):
            Square(10, 10, 1.5)

        with self.assertRaises(TypeError):
            Square(10, 10, True)

        with self.assertRaises(TypeError):
            Square(10, 10, False)

    def test_area(self):
        """Tests the area instance method
        """
        self.assertEqual(self.square_all_args.area(), 1)

    def test_to_dictionary(self):
        """Tests the to_dictionary instance method
        """
        self.assertEqual(
                         self.square_all_args.to_dictionary(),
                         {"id": 4, "size": 1, "x": 2, "y": 3}
                        )

    @patch('builtins.print')
    def test_display(self, mock_print):
        """Tests the instance method @display
        """
        self.square_all_args.display()
        mock_print.assert_called_once_with("\n\n\n  #")

    def test_str(self):
        """Tests the magic method @__str__
        """
        self.assertEqual(
                         self.square_all_args.__str__(),
                         "[Square] (4) 2/3 - 1"
                        )

    def test_update_args(self):
        """Tests the instance method @update with *args
        """
        self.square_all_args.update(89, 2, 3, 4)
        self.assertEqual(self.square_all_args.id, 89)
        self.assertEqual(self.square_all_args.size, 2)
        self.assertEqual(self.square_all_args.x, 3)
        self.assertEqual(self.square_all_args.y, 4)
        self.assertEqual(
                         self.square_all_args.to_dictionary(),
                         {"id": 89, "size": 2, "x": 3, "y": 4}
                        )

    def test_update_kwargs(self):
        """Tests the instance method @update with **kwargs
        """
        self.square_all_args.update(size=24, y=22, x=90, id=45)
        self.assertEqual(self.square_all_args.id, 45)
        self.assertEqual(self.square_all_args.size, 24)
        self.assertEqual(self.square_all_args.x, 90)
        self.assertEqual(self.square_all_args.y, 22)
        self.assertEqual(
                         self.square_all_args.to_dictionary(),
                         {"id": 45, "size": 24, "x": 90, "y": 22}
                        )

    def test_to_json_string(self):
        """Tests parent class static method to_json_string
        """
        dictionary = self.square_all_args.to_dictionary()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(
                         Base.to_json_string([dictionary]),
                         "[{\"id\": 4, \"size\": 1, \"x\": 2, \"y\": 3}]"
                        )

    def test_from_json_string(self):
        """Tests parent class static method from_json_string
        """
        json_list = [
                      self.square_all_args.to_dictionary(),
                      self.square_three_args.to_dictionary(),
                     ]
        list_input = Square.to_json_string(json_list)
        self.assertEqual(Square.from_json_string(None), "[]")
        self.assertEqual(
                         Square.from_json_string(list_input),
                         [
                          {
                           "id": 4,
                           "size": 1,
                           "x": 2,
                           "y": 3
                          },
                          {
                           "id": self.square_three_args.id,
                           "size": 1,
                           "x": 2,
                           "y": 3
                          }
                         ]
                        )
