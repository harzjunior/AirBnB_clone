#!/usr/bin/python3
import unittest
from models.amenity import Amenity

"""Unittest Module for the Amenity class"""

class TestAmenity(unittest.TestCase):
    '''Unit tests for the Amenity class'''

    def test_object_instantiation(self):
        '''Test instantiating the Amenity class'''
        self.amenity = Amenity()

    def testattr(self):
        '''Test the attributes of the Amenity class'''
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")

    def testsave(self):
        '''Test the save method'''
        self.amenity = Amenity()
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def teststr(self):
        '''Test the __str__ method to return the format of Amenity'''
        self.amenity = Amenity()
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))

if __name__ == '__main__':
    unittest.main()
