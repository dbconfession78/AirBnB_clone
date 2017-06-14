#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
"""Module: test_file_storage """


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""
    def setUp(self):
        """instantiate class"""
        self.filestorage = FileStorage()

    def test_attrs(self):
        """testing the attributes of FileStorage"""
        self.assertFalse(hasattr(self.filestorage, "random_attr"))

if "__main__" == __name__:
    unittest.main()
