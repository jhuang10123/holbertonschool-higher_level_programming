#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_noarguments(self):
        self.assertIsNone(max_integer())

    def test_str(self):
        self.assertEqual(max_integer("hungry"), "y")

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)


    @unittest.expectedFailure
    def test_wrong_type(self):
       with self.assertRaises(TypeError):
           max_integer(['x', 2, 1])




if __name__ == '__main__':
    unittest.main()
