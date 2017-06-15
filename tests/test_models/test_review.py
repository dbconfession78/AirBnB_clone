#!/usr/bin/python3
"""
Module: Unit Testing for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview class"""
    def setUp(self):
        """ instantiate class"""
        self.cls = Review()

    def testattr(self):
        """ testing  attributes"""
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "random_attr"))

        self.assertTrue(hasattr(self.cls, "place_id"))
        self.assertTrue(hasattr(self.cls, "user_id"))
        self.assertTrue(hasattr(self.cls, "text"))

        self.assertEqual(self.cls.__class__.__name__, "Review")
        self.assertEqual(self.cls.text, "")

        self.cls.text = "my review"
        self.assertEqual(self.cls.text, "my review")

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
        got = len(Review.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(Review.__init__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(Review.__str__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(Review.to_json.__doc__) > 0
        self.assertEqual(expected, got)
