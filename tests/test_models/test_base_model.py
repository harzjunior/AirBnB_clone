#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

"""Unit test Module for the BaseModel class"""

class TestBaseModel(unittest.TestCase):
    '''Unit tests for the BaseModel class'''

    def test_object_instantiation(self):
        '''Test instantiating the BaseModel class'''
        self.base_model = BaseModel()

    def test_checking_for_functions(self):
        '''Test checking the existence of docstrings'''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def testattr(self):
        '''Test BaseModel attributes'''
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertFalse(hasattr(self.base_model, "random_attr"))
        self.assertFalse(hasattr(self.base_model, "name"))
        self.assertTrue(hasattr(self.base_model, "id"))
        self.base_model.name = "Alice"
        self.base_model.age = "44"
        self.assertTrue(hasattr(self.base_model, "name"))
        self.assertTrue(hasattr(self.base_model, "age"))
        delattr(self.base_model, "name")
        self.assertFalse(hasattr(self.base_model, "name"))
        delattr(self.base_model, "age")
        self.assertFalse(hasattr(self.base_model, "age"))
        self.assertEqual(self.base_model.__class__.__name__, "BaseModel")

    def testsave(self):
        '''Test the save method'''
        self.base_model = BaseModel()
        self.base_model.save()
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def teststr(self):
        '''Test the __str__ method to return the format of BaseModel'''
        self.base_model = BaseModel()
        s = "[{}] ({}) {}".format(self.base_model.__class__.__name__,
                                  str(self.base_model.id),
                                  self.base_model.__dict__)
        self.assertEqual(print(s), print(self.base_model))

    def test_to_dict(self):
        '''Test the to_dict method'''
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
