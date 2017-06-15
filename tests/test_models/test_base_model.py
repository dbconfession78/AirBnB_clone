#!/usr/bin/python3

"""
Module: Unit Testing for BaseModel Class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class"""

    def setUp(self):
        """ instantiate BaseModel"""
        self.cls = BaseModel()

    def testattr(self):
        """ testing Amenity attributes"""
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertTrue(hasattr(self.cls, "id"))

        self.assertFalse(hasattr(self.cls, "random_attr"))
        self.assertFalse(hasattr(self.cls, "name"))

        self.cls.name = "Mike"
        self.cls.fave_color = "blue"
        self.assertTrue(hasattr(self.cls, "name"))
        self.assertEqual(self.cls.fave_color, "blue")
        delattr(self.cls, "name")
        self.assertFalse(hasattr(self.cls, "name"))
        self.assertEqual(self.cls.__class__.__name__, "BaseModel")

    def test_method(self):
        """testing  method"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(self.cls.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json(self):
        """to_json"""
        _json = self.cls.to_json()
        self.assertIsNotNone(_json.get("id"))

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(BaseModel.__doc__) > 0
        self.assertEqual(expected, got)

    def test_save_doc(self):
        """save() documentation"""
        expected = True
        got = len(BaseModel.save.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(BaseModel.__init__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_to_json_doc(self):
        """to_json() documentation"""
        expected = True
        got = len(BaseModel.to_json.__doc__) > 0
        self.assertEqual(expected, got)

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(BaseModel.__str__.__doc__) > 0
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main
