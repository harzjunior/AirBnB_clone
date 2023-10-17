#!/usr/bin/python3
import unittest
from models.review import Review
"""Unit test Module for the Review class"""

class TestUser(unittest.TestCase):
    '''Unit tests for the Review class'''

    def test_object_Instantiation(self):
        '''Test instantiating the Review class'''
        self.review = Review()

    def testattr(self):
        '''Test Review attributes'''
        self.review = Review()
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertFalse(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def testsave(self):
        '''Test the save method'''
        self.review = Review()
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def teststr(self):
        '''Test the __str__ method to return the format of Review'''
        self.review = Review()
        s = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                  str(self.review.id), self.review.__dict__)
        self.assertEqual(print(s), print(self.review))

if __name__ == '__main__':
    unittest.main()
