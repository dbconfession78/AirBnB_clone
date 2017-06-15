#!/usr/bin/python3
"""
Module: Unit Testing for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace class"""
    def setUp(self):
        """ instantiate class"""
        self.cls = Place()

    def testattr(self):
        """ testing  attributes"""
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "random_attr"))

        self.assertTrue(hasattr(self.cls, "city_id"))
        self.assertTrue(hasattr(self.cls, "user_id"))
        self.assertTrue(hasattr(self.cls, "name"))
        self.assertTrue(hasattr(self.cls, "description"))
        self.assertTrue(hasattr(self.cls, "number_rooms"))
        self.assertTrue(hasattr(self.cls, "number_bathrooms"))
        self.assertTrue(hasattr(self.cls, "max_guest"))
        self.assertTrue(hasattr(self.cls, "price_by_night"))
        self.assertTrue(hasattr(self.cls, "latitude"))
        self.assertTrue(hasattr(self.cls, "longitude"))
        self.assertTrue(hasattr(self.cls, "amenity_ids"))

        self.assertEqual(self.cls.__class__.__name__, "Place")
        self.assertEqual(self.cls.name, "")

        self.cls.name = "Red House"
        self.assertEqual(self.cls.name, "Red House")

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
        got = len(Place.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(Place.__init__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(Place.__str__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(Place.to_json.__doc__) > 0
        self.assertEqual(expected, got)
