#!/usr/bin/python3
"""
Module: Unit Testing for FileStorage
"""
import unittest
from models.engine import file_storage
from datetime import datetime

FS = file_storage.FileStorage


class TestDocumentation(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    @classmethod
    def setUpClass(cls):
        """ Documentation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("              FileStorage              ")
        print("           Documentation Tests         ")
        print("=======================================")
        print("")

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(file_storage.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(FileStorage.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(FileStorage.__init__.__doc__) > 0
        self. assertEqual(expected, got)


class TestMethods(unittest.TestCase):
    """ class method and instantisation tests """

    @classmethod
    def setUpClass(cls):
        """ Method Testing Set-up"""

        print("\n")
        print("=======================================")
        print("               FileStorage             ")
        print("              Method Tests             ")
        print("=======================================")
        print("")

    def test_instantiation(self):
        """ Instantiation"""
        cls = FileStoragel()
        self.assertIsInstance(cls, FileStorage)

    def test_string_format(self):
        """String formatting"""
        cls = City()
        expected = "[{}] ({}) {}".format(cls.__class__.__name__,
                                         str(cls.id), cls.__dict__)
        got = str(cls)
        self.assertEqual(expected, got)

    def test_name_attr(self):
        """name attribute"""
        cls = FileStorage()
        expected = "XXX"
        got = "XXX"

        self.assertEqual(expected, got)

    def test_number_attr(self):
        """number attribute"""
        cls = FileStorage()
        expected = "XXX"
        got = "XXX"
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
