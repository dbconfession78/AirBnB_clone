#!/usr/bin/python3
"""
Module: Unit Testing for Amenity Class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestAmenity class"""

    def setUp(self):
        """ instantiate Amenity"""
        self.amenity = Amenity()

    def testattr(self):
        """ testing Amenity attributes"""
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertFalse(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertEqual(self.amenity.name, "")

    def test_method(self):
        """testing Amenity methods"""
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_string_format(self):
        """testing string formatting"""
        expected = "[{}] ({}) {}".format(
            self.amenity.__class__.__name__, str(
                self.amenity.id), self.amenity.__dict__)
        got = str(self.amenity)
        self.assertEqual(expected, got)

    def test_module_doc(self):
        """ tests for presence module documentation """
        expected = True
        got = len(self.amenity.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(Amenity.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(Amenity.__init__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(Amenity.to_json.__doc__) > 0
        self.assertEqual(expected, got)

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(Amenity.__str__.__doc__) > 0
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
