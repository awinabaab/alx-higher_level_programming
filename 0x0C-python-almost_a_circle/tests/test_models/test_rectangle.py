#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from os import remove
import csv


class TestRectangle(unittest.TestCase):
    """A class to test Base class instances
    """

    def setUp(self):
        """Setups an instance
        """
        self.rect_all_args = Rectangle(1, 2, 3, 4, 5)
        self.rect_two_args = Rectangle(1, 2)
        self.rect_three_args = Rectangle(1, 2, 3)
        self.rect_four_args = Rectangle(1, 2, 3, 4)

    def tearDown(self):
        """Deletes an instance
        """
        del self

    def test_rect_no_arg(self):
        """Test initialization with no args
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_one_arg(self):
        """Test initialization with one arg @width
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rect_two_args(self):
        """Test initialization with two args @width and @height
        """
        self.assertEqual(self.rect_two_args.id, self.rect_two_args.id)
        self.assertEqual(self.rect_two_args.width, 1)
        self.assertEqual(self.rect_two_args.height, 2)
        self.assertEqual(self.rect_two_args.x, 0)
        self.assertEqual(self.rect_two_args.y, 0)

    def test_rect_three_args(self):
        """Test initialization with three args @width, @height and @x
        """
        self.assertEqual(self.rect_three_args.id, self.rect_three_args.id)
        self.assertEqual(self.rect_three_args.width, 1)
        self.assertEqual(self.rect_three_args.height, 2)
        self.assertEqual(self.rect_three_args.x, 3)
        self.assertEqual(self.rect_three_args.y, 0)

    def test_rect_four_args(self):
        """Test initialization with four args @width, @height, @x and @y
        """
        self.assertEqual(self.rect_four_args.id, self.rect_four_args.id)
        self.assertEqual(self.rect_four_args.width, 1)
        self.assertEqual(self.rect_four_args.height, 2)
        self.assertEqual(self.rect_four_args.x, 3)
        self.assertEqual(self.rect_four_args.y, 4)

    def test_rect_all_args(self):
        """Test initialization with all args @width, @height, @x, @y and @id
        """
        self.assertEqual(self.rect_all_args.id, 5)
        self.assertEqual(self.rect_all_args.width, 1)
        self.assertEqual(self.rect_all_args.height, 2)
        self.assertEqual(self.rect_all_args.x, 3)
        self.assertEqual(self.rect_all_args.y, 4)

    def test_rect_width_setter(self):
        """Test instance width setter
        """
        with self.assertRaises(TypeError):
            Rectangle("a", 10)

        with self.assertRaises(ValueError):
            Rectangle(0, 10)

        with self.assertRaises(TypeError):
            Rectangle(10.5, 10)

        with self.assertRaises(TypeError):
            Rectangle(True, 10)

        with self.assertRaises(TypeError):
            Rectangle(False, 10)

    def test_rect_width_getter(self):
        """Test instance attribute width getter
        """
        self.assertEqual(self.rect_all_args.width, 1)

    def test_rect_height_setter(self):
        """Test instance height setter
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "a")

        with self.assertRaises(ValueError):
            Rectangle(10, 0)

        with self.assertRaises(TypeError):
            Rectangle(10, 10.5)

        with self.assertRaises(TypeError):
            Rectangle(10, True)

        with self.assertRaises(TypeError):
            Rectangle(10, False)

    def test_rect_height_getter(self):
        """Test instance attribute height getter
        """
        self.assertEqual(self.rect_all_args.height, 2)

    def test_rect_x_setter(self):
        """Test instance height setter
        """
        with self.assertRaises(TypeError):
            Rectangle(10, 10, "x")

        with self.assertRaises(ValueError):
            Rectangle(10, 10, -1)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, 1.5)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, True)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, False)

    def test_rect_x_getter(self):
        """Test instance attribute x getter
        """
        self.assertEqual(self.rect_all_args.x, 3)

    def test_rect_y_setter(self):
        """Test instance height setter
        """
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 10, "y")

        with self.assertRaises(ValueError):
            Rectangle(10, 10, 1, -1)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, 1, 1.5)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, 10, True)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, 10, False)

    def test_rect_y_getter(self):
        """Test instance attribute y getter
        """
        self.assertEqual(self.rect_all_args.y, 4)

    def test_area(self):
        """Tests the area instance method
        """
        self.assertEqual(self.rect_all_args.area(), 2)

    def test_to_dictionary(self):
        """Tests the to_dictionary instance method
        """
        self.assertEqual(
                         self.rect_all_args.to_dictionary(),
                         {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
                        )

    @patch('builtins.print')
    def test_display(self, mock_print):
        """Tests the instance method @display
        """
        self.rect_all_args.display()
        mock_print.assert_called_once_with("\n\n\n\n   #\n   #")

    def test_str(self):
        """Tests the magic method @__str__
        """
        self.assertEqual(
                         str(self.rect_all_args),
                         "[Rectangle] (5) 3/4 - 1/2"
                        )

    def test_update_args(self):
        """Tests the instance method @update with *args
        """
        self.rect_all_args.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rect_all_args.id, 89)
        self.assertEqual(self.rect_all_args.width, 2)
        self.assertEqual(self.rect_all_args.height, 3)
        self.assertEqual(self.rect_all_args.x, 4)
        self.assertEqual(self.rect_all_args.y, 5)
        self.assertEqual(
                         self.rect_all_args.to_dictionary(),
                         {"id": 89, "width": 2, "height": 3, "x": 4, "y": 5}
                        )

    def test_update_kwargs(self):
        """Tests the instance method @update with **kwargs
        """
        self.rect_all_args.update(height=12, width=4, y=22, x=90, id=45)
        self.assertEqual(self.rect_all_args.id, 45)
        self.assertEqual(self.rect_all_args.width, 4)
        self.assertEqual(self.rect_all_args.height, 12)
        self.assertEqual(self.rect_all_args.x, 90)
        self.assertEqual(self.rect_all_args.y, 22)
        self.assertEqual(
                         self.rect_all_args.to_dictionary(),
                         {"id": 45, "width": 4, "height": 12, "x": 90, "y": 22}
                        )

    def test_to_json_string(self):
        """Tests parent class static method to_json_string
        """
        dictionary = self.rect_all_args.to_dictionary()
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(
                         Rectangle.to_json_string([dictionary]),
                         "[{\"id\": 5, \"width\": 1, \
\"height\": 2, \"x\": 3, \"y\": 4}]"
                        )

    def test_from_json_string(self):
        """Tests parent class static method from_json_string
        """
        json_list = [
                      self.rect_all_args.to_dictionary(),
                      self.rect_four_args.to_dictionary(),
                     ]
        list_input = Rectangle.to_json_string(json_list)
        self.assertEqual(Rectangle.from_json_string(None), "[]")
        self.assertEqual(
                         Rectangle.from_json_string(list_input),
                         [
                          {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4},
                          {"id": 17, "width": 1, "height": 2, "x": 3, "y": 4},
                         ]
                        )

    def test_save_to_file(self):
        """Tests parent class method save_to_file
        """
        Rectangle.save_to_file([self.rect_three_args, self.rect_all_args])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            contents = Rectangle.from_json_string(content)
            self.assertEqual(contents[0], self.rect_three_args.to_dictionary())
            self.assertEqual(contents[1], self.rect_all_args.to_dictionary())
        # Testing with None value
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
            contents = Rectangle.from_json_string(content)
            self.assertEqual(contents, [])
        remove("Rectangle.json")

    def test_load_from_file_exists(self):
        """Tests parent class method load_from_file
        """
        Rectangle.save_to_file([self.rect_three_args, self.rect_all_args])
        contents = Rectangle.load_from_file()

        self.assertEqual(contents[0].id, self.rect_three_args.id)
        self.assertEqual(contents[1].id, self.rect_all_args.id)
        remove("Rectangle.json")

    def test_load_from_file_non_existent(self):
        """Tests parent class method load_from_file
        """
        contents = Rectangle.load_from_file()
        self.assertEqual(contents, [])

    def test_save_to_file_csv(self):
        """Tests parent class method save_to_file
        """
        Rectangle.save_to_file_csv([self.rect_three_args, self.rect_all_args])
        with open("Rectangle.csv", "r") as f:
            reader = csv.reader(f, delimiter=",", lineterminator="\n")
            contents = [item for item in reader]
            self.assertEqual(int(contents[0][0]), self.rect_three_args.id)
            self.assertEqual(int(contents[1][0]), self.rect_all_args.id)
        # Testing with None value
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            reader = csv.reader(f, delimiter=",", lineterminator="\n")
            contents = [item for item in reader]
            self.assertEqual(contents[0], [])
        remove("Rectangle.csv")

    def test_load_from_file_csv_exists(self):
        """Tests parent class method load_from_file
        """
        Rectangle.save_to_file_csv([self.rect_three_args, self.rect_all_args])
        contents = Rectangle.load_from_file_csv()

        self.assertEqual(contents[0].id, self.rect_three_args.id)
        self.assertEqual(contents[1].id, self.rect_all_args.id)
        remove("Rectangle.csv")

    def test_load_from_file_csv_non_existent(self):
        """Tests parent class method load_from_file
        """
        contents = Rectangle.load_from_file_csv()
        self.assertEqual(contents, [])
