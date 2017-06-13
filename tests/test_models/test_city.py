#!/usr/bin/python3
"""
Module: Unit Testing for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """TestCity class"""
    def setUp(self):
        """ instantiate Amenity"""
        self.city = City()

    def testattr(self):
        """ testing Amenity attributes"""
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertFalse(hasattr(self.city, "updated_at"))
        self.assertFalse(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.__class__.__name__, "City")
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "San Francisco"
        self.state_id = "343r387"
        self.assertEqual(self.city.name, "San Francisco")

    def test_method(self):
        """testing Amenity methods"""
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_string_format(self):
        """testing string formatting"""
        expected = "[{}] ({}) {}".format(
            self.city.__class__.__name__, str(
                self.city.id), self.city.__dict__)
        got = str(self.city)
        self.assertEqual(expected, got)

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(self.city.__doc__) > 0
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

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(City.__str__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(City.to_json.__doc__) > 0
        self.assertEqual(expected, got)
