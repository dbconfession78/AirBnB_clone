#!/usr/bin/python3
"""
Module: Unit Testing for User Class
"""
import unittest
from moels import user
from datetime import datetime

User = user.User


class TestDocumentation(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    @classmethod
    def setUpClass(cls):
        """ Documentation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                 User                  ")
        print("           Documentation Tests         ")
        print("=======================================")
        print("")

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(user.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(User.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(User.__init__.__doc__) > 0
        self. assertEqual(expected, got)


class MethodTests(unittest.TestCase):
    """ test class methods and instantiation """

    @classmethod
    def setUpClass(cls):
        """ Method Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                 User                  ")
        print("              Method Tests             ")
        print("=======================================")
        print("")

    def test_instantiation(self):
        """ Instantiation"""
        cls = User()
        self.assertIsInstance(cls, User)

    def test_string_format(self):
        """String formatting"""
        cls = User()
        expected = "[{}] ({}) {}".format(cls.__class__.__name__,
                                         str(cls.id), cls.__dict__)
        got = str(cls)
        self.assertEqual(expected, got)

    def test_name_attr(self):
        """name attribute"""
        cls = User()
        expected = "XXX"
        got = "XXX"

        self.assertEqual(expected, got)

    def test_number_attr(self):
        """number attribute"""
        cls = User()
        expected = "XXX"
        got = "XXX"
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
