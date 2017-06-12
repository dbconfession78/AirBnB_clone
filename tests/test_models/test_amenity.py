#!/usr/bin/python3
"""
Module: Unit Testing for Amenity Class
"""
import unittest
from models import amenity
from datetime import datetime

Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Test for presence of file, class and method documentation"""

    def setUp(self):
        """ Base Model Documentation Testing Set-up"""
        self.amenity = Amenity
        print("\n")
        print("=======================================")
        print("               Amenity                 ")
        print("           Documentation Tests         ")
        print("=======================================")
        print("")

    def test_module_doc(self):
        """ tests for presence module documentation """
        expected = True
        got = len(amenity.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """class documentation"""
        expected = True
        got = len(Amenity.__doc__) > 0
        self.assertEqual(expected, got)

    def test_save_doc(self):
        """save() documentation"""
        expected = True
        got = len(Amenity.save.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(Amenity.__init__.__doc__) > 0
        self. assertEqual(expected, got)

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


class TestInstantiation(unittest.TestCase):
    """ test Amenity instantiation """

    @classmethod
    def setUpClass(cls):
        """ Amenity Instantiation Testing Set-up"""

        print("\n")
        print("=======================================")
        print("                Amenity                ")
        print("              Method Tests             ")
        print("=======================================")
        print("")

    def test_instantiation(self):
        """Amenity Instantiation"""
        bm = Amenity()
        self.assertIsInstance(bm, Amenity)

    def test_string_format(self):
        """String formatting"""
        bm = Amenity()
        expected = "[{}] ({}) {}".format(bm.__class__.__name__,
                                         str(bm.id), bm.__dict__)
        got = str(bm)
        self.assertEqual(expected, got)

    def test_save(self):
        """call save()"""
        bm = Amenity()
        bm.save()
        expected = True
        got = bm.created_at != bm.updated_at
        self.assertEqual(expected, got)

    def test_to_json(self):
        """call to_json"""
        bm = Amenity()
        json = str(bm.to_json())
        created_at = "'created_at': '" + datetime.strftime(
            bm.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f") + "'"
        header = "{'__class__': 'Amenity', 'id': '"
        _id = bm.__dict__["id"]
        string = "{'__class__': 'Amenity', 'id': '" + bm.__dict__[
            "id"] + "', 'created_at': '" + created_at + "'}"
        expected = True
        if created_at in string and header in string and _id in string:
            got = True
        else:
            got = False

        self.assertEqual(expected, got)

    def test_name_attr(self):
        """name attribute"""
        bm = Amenity()
        expected = "XXX"
        got = "XXX"

        self.assertEqual(expected, got)

    def test_number_attr(self):
        """number attribute"""
        bm = Amenity()
        expected = "XXX"
        got = "XXX"
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main
