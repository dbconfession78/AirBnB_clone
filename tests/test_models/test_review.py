#!/usr/bin/python3
"""
Module: Unit Testing for Review Class
"""
import unittest
from models import review
from datetime import datetime

Review = review.Review


class TestDocumentation(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    @classmethod
    def setUpClass(cls):
        """ Documentation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                 Review                ")
        print("           Documentation Tests         ")
        print("=======================================")
        print("")

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(review.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(Review.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(Review.__init__.__doc__) > 0
        self. assertEqual(expected, got)


class MethodTests(unittest.TestCase):
    """ test class methods and instantiation """

    @classmethod
    def setUpClass(cls):
        """ Method Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                 Review                ")
        print("              Method Tests             ")
        print("=======================================")
        print("")

    def test_instantiation(self):
        """ Instantiation"""
        cls = Review()
        self.assertIsInstance(cls, Review)

    def test_string_format(self):
        """String formatting"""
        cls = Review()
        expected = "[{}] ({}) {}".format(cls.__class__.__name__,
                                         str(cls.id), cls.__dict__)
        got = str(cls)
        self.assertEqual(expected, got)

    def test_name_attr(self):
        """name attribute"""
        cls = Review()
        expected = "XXX"
        got = "XXX"

        self.assertEqual(expected, got)

    def test_number_attr(self):
        """number attribute"""
        cls = Review()
        expected = "XXX"
        got = "XXX"
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
