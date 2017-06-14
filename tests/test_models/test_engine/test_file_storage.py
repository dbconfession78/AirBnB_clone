#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models import storage
"""Module: test_file_storage """


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""
    def setUp(self):
        """instantiate class"""
        self.cls = FileStorage()

    def test_attrs(self):
        """testing the attributes of FileStorage"""
        self.assertFalse(hasattr(self.cls, "random_attr"))
        self.assertTrue(hasattr(self.cls, "class_models"))


    def test_instqntiation(self):
        """ instatiate class """
        self.assertIsInstance(storage, FileStorage)

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

    def test_all_doc(self):
        """ all() method documentation"""
        expected = True
        got = len(FileStorage.all.__doc__) > 0
        self.assertEqual(expected, got)

    def test_new_doc(self):
        """ new() method documentation """
        expected = True
        got = len(FileStorage.new.__doc__) > 0
        self.assertEqual(expected, got)

    def test_new_doc(self):
        """ save() method documentation """
        expected = True
        got = len(FileStorage.save.__doc__) > 0
        self.assertEqual(expected, got)

    def test_reload_doc(self):
        """ reload() method documentation """
        expected = True
        got = len(FileStorage.reload.__doc__) > 0
        self.assertEqual(expected, got)

if "__main__" == __name__:
    unittest.main()
