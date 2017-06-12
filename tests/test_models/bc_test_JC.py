#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from models import base_model
BaseModel = base_model.BaseModel

class TestBaseModelDocumentation(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.....  For BaseModel Class  .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nBaseModel Class of Models Module\n'
        actual = models.base_model.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'attributes and functions for BaseModel class'
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiation of new BaseModel Class'
        actual = BaseModel.__init__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = 'updates attribute updated_at to current time'
        actual = BaseModel.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_to_json(self):
        """... documentation for to_json function"""
        expected = 'returns json representation of self'
        actual = BaseModel.to_json.__doc__
        self.assertEqual(expected, actual)

    def test_doc_str(self):
        """... documentation for to str function"""
        expected = 'returns string type representation of object instance'
        actual = BaseModel.__str__.__doc__
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main
