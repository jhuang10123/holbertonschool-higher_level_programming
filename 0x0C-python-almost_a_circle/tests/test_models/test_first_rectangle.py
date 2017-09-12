#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models import rectangle
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Presence of docstrings"""
    def test_presence_of_module_docstring(self):
        module_doc = rectangle.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        class_doc = Rectangle.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        init_doc = Rectangle.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)


if __name__ == "__main__":
    unittest.main()
