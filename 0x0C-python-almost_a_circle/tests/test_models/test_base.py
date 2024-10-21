#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class to test Base class instances
    """

    def setUp(self):
        """Setups an instance
        """
        self.base_none = Base(None)
        self.base_pos_int = Base(10)
        self.base_neg_int = Base(-10)
        self.base_zero = Base(0)
        self.base_list = Base(list())
        self.base_dict = Base(dict())
        self.base_set = Base(set())
        self.base_tuple = Base(tuple())

    def tearDown(self):
        """Deletes an instance
        """
        del self

    def test_id_none(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_none.id, 4)
        self.tearDown()

    def test_id_pos_int(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_pos_int.id, 10)
        self.tearDown()

    def test_id_neg_int(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_neg_int.id, -10)
        self.tearDown()

    def test_id_zero(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_zero.id, 0)
        self.tearDown()

    def test_id_list(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_list.id, [])
        self.tearDown()

    def test_id_dict(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_dict.id, {})
        self.tearDown()

    def test_id_set(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_set.id, set())
        self.tearDown()

    def test_id_tuple(self):
        """Tests the id of an instance with a None value
        """
        self.assertEqual(self.base_tuple.id, ())
        self.tearDown()


if __name__ == "__main__":
    unittest.main()
