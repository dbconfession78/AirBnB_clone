#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
"""Module: test_file_storage """


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""
    def setUp(self):
        """instantiate class"""
        self.cls = FileStorage()

    def test_attrs(self):
        """testing the attributes of FileStorage"""
        self.assertFalse(hasattr(self.cls, "random_attr"))

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(self.cls.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """ class documentation """
        expected = True
        got = len(FileStorage.__doc__) > 0
        self.assertEqual(expected, got)

        def test_init_doc(self):
            """__init__() documentation"""
            expected = True
            got = len(FileStorage.__init__.__doc__) > 0
            self.assertEqual(expected, got)

if "__main__" == __name__:
    unittest.main()
