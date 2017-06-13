#!/usr/bin/python3
"""
Module: Unit Testing for State class
"""
import unittest
from models.state import State


class TestCity(unittest.TestCase):
    """TestState class"""
    def setUp(self):
        """ instantiate Amenity"""
        self.cls = State()

    def testattr(self):
        """ testing Amenity attributes"""
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "random_attr"))
        self.assertTrue(hasattr(self.cls, "name"))
        self.assertEqual(self.cls.__class__.__name__, "State")
        self.assertEqual(self.cls.name, "")

        self.cls.name = "New Jersey"
        self.assertEqual(self.cls.name, "New Jersey")

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
        got = len(State.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(State.__init__.__doc__) > 0
        self. assertEqual(expected, got)

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(State.__str__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(State.to_json.__doc__) > 0
        self.assertEqual(expected, got)
