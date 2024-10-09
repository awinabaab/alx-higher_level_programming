#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class to test max_integer[..]
    """

    def test_max_integer(self):
        """A function to test max_integer([..])
        """

        # Testing with lists
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1.2, 2.4, 3.6, 4.8, 5.10]), 5.1)

        with self.assertRaises(TypeError):
            max_integer(['a', 98, 'c', 100, 'e'])

        self.assertEqual(max_integer(['a', 'b', 'c', 'd', 'e']), 'e')
        self.assertEqual(max_integer(["Kwadwo", "Kwabena", "Kweku",
                                     "Yaw", "Kofi"]), "Yaw")

        # Testing with tuples
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer((1, 2, 3, 4, 5)), 5)
        self.assertEqual(max_integer((1.2, 2.4, 3.6, 4.8, 5.10)), 5.1)

        with self.assertRaises(TypeError):
            max_integer(('a', 98, 'c', 100, 'e'))

        self.assertEqual(max_integer(('a', 'b', 'c', 'd', 'e')), 'e')
        self.assertEqual(max_integer(("Kwadwo", "Kwabena", "Kweku",
                                     "Yaw", "Kofi")), "Yaw")

        # Testing with dictionaries
        self.assertEqual(max_integer({}), None)
        with self.assertRaises(KeyError):
            max_integer({'a': 97, 'b': 98, 'c': 99, 'd': 100})

        # Testing with sets
        self.assertEqual(max_integer(set()), None)
        with self.assertRaises(TypeError):
            max_integer(set((1, 2, 3, 4, 5)))

        with self.assertRaises(TypeError):
            max_integer(set(('a', 'b', 'v', 'f', 'g')))

        # Testing with integers
        with self.assertRaises(TypeError):
            max_integer(78)

        self.assertEqual(max_integer([10, 8, 6, 4, 2]), 10)
        self.assertEqual(max_integer([10]), 10)

        # Testing with floats
        with self.assertRaises(TypeError):
            max_integer(50.78)

        # Testing with strings
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer("Kwadwo"), 'w')
        self.assertEqual(max_integer("6349q9742"), 'q')

        # Testing with complex numbers
        with self.assertRaises(TypeError):
            max_integer([2j, 4j, 10j, 8j, 6j])

        with self.assertRaises(TypeError):
            max_integer([2.2j, 4.8j, 10.20j, 8.16j, 6.12j])


if __name__ == "__main__":
    unittest.main()
