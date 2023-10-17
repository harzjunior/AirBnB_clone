#!/usr/bin/python3
import unittest
from models.city import City

"""Unit test Module for the City class"""

class TestCity(unittest.TestCase):
    '''Unit tests for the City class'''

    def test_object_instantiation(self):
        '''Test instantiating the City class'''
        self.city = City()

    def testattr(self):
        '''Test City attributes'''
        self.city = City()
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertFalse(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "WonderLand"
        self.city.state_id = "Won67L0nd"
        self.assertEqual(self.city.name, "WonderLand")
        self.assertEqual(self.city.state_id, "Won67L0nd")
        self.assertEqual(self.city.__class__.__name__, "City")

    def testsave(self):
        '''Test the save method'''
        self.city = City()
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def teststr(self):
        '''Test the __str__ method to return the format of City'''
        self.city = City()
        s = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                  str(self.city.id),
                                  self.city.__dict__)
        self.assertEqual(print(s), print(self.city))

if __name__ == '__main__':
    unittest.main()
