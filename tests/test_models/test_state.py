#!/usr/bin/python3
import unittest
from models.state import State
"""Unit test Module for the Review class"""

class TestUser(unittest.TestCase):
    '''Unit tests for the Review class'''

    def test_object_Instantiation(self):
        '''Test instantiating the Review class'''
        self.state = State()

    def testattr(self):
        '''Test Review attributes'''
        self.state = State()
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertFalse(hasattr(self.state, "random_attr"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertEqual(self.state.name, "")
        self.state.name = "WonderLand"
        self.assertEqual(self.state.name, "WonderLand")
        self.assertEqual(self.state.__class__.__name__, "State")

    def testsave(self):
        '''Test the save method'''
        self.state = State()
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def teststr(self):
        '''Test the __str__ method to return the format of Review'''
        self.state = State()
        s = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                  str(self.state.id), self.state.__dict__)
        self.assertEqual(print(s), print(self.state))

if __name__ == '__main__':
    unittest.main()
