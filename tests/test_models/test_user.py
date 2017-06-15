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
        self.user = User()

    def test_attr(self):
        """ testing  attributes"""
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertFalse(hasattr(self.user, "updated_at"))
        self.assertFalse(hasattr(self.user, "random_attr"))

        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

        self.assertEqual(self.user.__class__.__name__, "User")
        self.assertEqual(self.user.first_name, "")

        self.user.first_name = "Betty"
        self.assertEqual(self.user.first_name, "Betty")

        # last name
        self.assertEqual(self.user.last_name, "")
        self.user.last_name = "Kuredjian"
        self.assertEqual(self.user.last_name, "Kuredjian")

        # email
        self.assertEqual(self.user.email, "")
        self.user.email = "katya@holbertonschool.com"
        self.assertEqual(self.user.email, "katya@holbertonschool.com")

        # pw
        self.assertEqual(self.user.password, "")
        self.user.password = "my_pw"
        self.assertEqual(self.user.password, "my_pw")

    def test_method(self):
        """testing Amenity methods"""
        self.user.save()
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_string_format(self):
        """testing string formatting"""
        expected = "[{}] ({}) {}".format(
            self.user.__class__.__name__, str(
                self.user.id), self.user.__dict__)
        got = str(self.user)
        self.assertEqual(expected, got)

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(self.user.__doc__) > 0
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
        self.assertEqual(expected, got)

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
