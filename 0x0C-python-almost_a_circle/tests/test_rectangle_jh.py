#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest

"""
from models import base
from models.base import Base
"""

class TestRectangle(unittest.TestCase):
    """Presence of docstrings"""
    def test_presence_of_module_docstring(self):
        module_doc = base.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        init_doc = Base.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)


    def test_failures(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
"""
    def setUp(self):
        self.base = Base()

    def tearDown(self):
        del self.base
"""
"""
    def test_failures(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
"""

if __name__ == "__main__":
    unittest.main()



"""
- error messages

"""
