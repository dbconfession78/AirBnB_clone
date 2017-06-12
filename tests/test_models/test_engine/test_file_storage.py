#!/usr/bin/python3
"""
Module: Unit Testing for City Class
"""
import unittest
from models import city
from datetime import datetime

City = city.City


class TestDocumentation(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    @classmethod
    def setUpClass(cls):
        """ Documentation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                  City                 ")
        print("           Documentation Tests         ")
        print("=======================================")
        print("")

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(city.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(City.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(City.__init__.__doc__) > 0
        self. assertEqual(expected, got)


class TestInstantiation(unittest.TestCase):
    """ test instantiation """

    @classmethod
    def setUpClass(cls):
        """ Method Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                  City                 ")
        print("              Method Tests             ")
        print("=======================================")
        print("")

    def test_instantiation(self):
        """ Instantiation"""
        cty = Cityl()
        self.assertIsInstance(cty, City)

    def test_string_format(self):
        """String formatting"""
        cty = City()
        expected = "[{}] ({}) {}".format(cty.__class__.__name__,
                                         str(cty.id), cty.__dict__)
        got = str(cty)
        self.assertEqual(expected, got)

    def test_name_attr(self):
        """name attribute"""
        cty = City()
        expected = "XXX"
        got = "XXX"

        self.assertEqual(expected, got)

    def test_number_attr(self):
        """number attribute"""
        cty = City()
        expected = "XXX"
        got = "XXX"
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
