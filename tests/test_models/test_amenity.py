#!/usr/bin/python3
import unittest
from models import amenity
"""module: amenity_test"""


Amenity = amenity.Amenity

class TestAmenity(unittest.TestCase):
    """Class: TestAmenity"""
    def setUp(self):
        """instance setup"""
        self.amenity = Amenity()

    def testattr(self):
        """Testing the attributes of Amenity"""
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertFalse(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertEqual(self.amenity.name, "")

    def testmethod(self):
        """Testing the methods of Amenity"""
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def teststr(self):
        """Testing the str format of Amenity"""
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id),
                                  self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))

if __name__ == '__main__':
    unittest.main()
