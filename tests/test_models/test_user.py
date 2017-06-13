#!/usr/bin/python3
"""
Module: Unit Testing for User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser class"""
    def setUp(self):
        """ instantiate class"""
        self.cls = User()

    def testattr(self):
        """ testing  attributes"""
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "random_attr"))

        self.assertTrue(hasattr(self.cls, "email"))
        self.assertTrue(hasattr(self.cls, "password"))
        self.assertTrue(hasattr(self.cls, "first_name"))
        self.assertTrue(hasattr(self.cls, "last_name"))

        self.assertEqual(self.cls.__class__.__name__, "User")
        self.assertEqual(self.cls.first_name, "")

        self.cls.first_name = "Betty"
        self.assertEqual(self.cls.first_name, "Betty")

    def test_method(self):
        """testing Amenity methods"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def test_string_format(self):
        """testing string formatting"""
        expected = "[{}] ({}) {}".format(
            self.cls.__class__.__name__, str(
                self.cls.id), self.cls.__dict__)
        got = str(self.cls)
        self.assertEqual(expected, got)

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(self.cls.__doc__) > 0
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

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(User.__str__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(User.to_json.__doc__) > 0
        self.assertEqual(expected, got)
