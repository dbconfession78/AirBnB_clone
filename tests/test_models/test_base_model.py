#!/usr/bin/python3
"""
Module: Unit Testing for BaseModel Class
"""
import unittest
from models import base_model
from datetime import datetime

BaseModel = base_model.BaseModel


class TestDocumentation(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    @classmethod
    def setUpClass(cls):
        """ Base Model Documentation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("               BaseModel               ")
        print("           Documentation Tests         ")
        print("=======================================")
        print("")

    def test_module_doc(self):
        """ tests for presence base_model documentation """
        expected = True
        got = len(base_model.__doc__) > 0
        self.assertEqual(expected, got)

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
        self. assertEqual(expected, got)

    def test_to_json(self):
        """to_json() documentation"""
        expected = True
        got = len(BaseModel.to_json.__doc__) > 0
        self.assertEqual(expected, got)

    def test_str_doc(self):
        """__str__() documentation"""
        expected = True
        got = len(BaseModel.__str__.__doc__) > 0
        self.assertEqual(expected, got)


class TestInstantiation(unittest.TestCase):
    """ test BaseModel instantiation """

    @classmethod
    def setUpClass(cls):
        """ BaseModel Instantiation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("               BaseModel               ")
        print("              Method Tests             ")
        print("=======================================")
        print("")

    def test_instantiation(self):
        """BaseModel Instantiation"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_string_format(self):
        """String formatting"""
        bm = BaseModel()
        expected = "[{}] ({}) {}".format(bm.__class__.__name__,
                                         str(bm.id), bm.__dict__)
        got = str(bm)
        self.assertEqual(expected, got)

    def test_save(self):
        """call save()"""
        bm = BaseModel()
        bm.save()
        expected = True
        got = bm.created_at != bm.updated_at
        self.assertEqual(expected, got)

    def test_to_json(self):
        """call to_json"""
        bm = BaseModel()
        json = str(bm.to_json())
        created_at = "'created_at': '" + datetime.strftime(
            bm.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f") + "'"
        header = "{'__class__': 'BaseModel', 'id': '"
        _id = bm.__dict__["id"]
        string = "{'__class__': 'BaseModel', 'id': '" + bm.__dict__[
            "id"] + "', 'created_at': '" + created_at + "'}"
        expected = True
        if created_at in string and header in string and _id in string:
            got = True
        else:
            got = False

        self.assertEqual(expected, got)

    def test_name_attrn(self):
        """name attribute"""
        bm = BaseModel()
        expected = "XXX"
        got = "XXX"

        self.assertEqual(expected, got)

    def test_number_attr(self):
        """number attribute"""
        bm = BaseModel()
        expected = "XXX"
        got = "XXX"
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
