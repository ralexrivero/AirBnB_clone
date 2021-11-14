#!/usr/bin/python3
""" unittest for models/base_model.py

    test classes:
        test_BaseModel_instantiation
        test_BaseModel_save
        test_BaseModel_to_dict
        test_BaseModel_str
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class test_BaseModel_instantiation(unittest.TestCase):
    """ test instantiation of BaseModel """
    def test_BaseModel_instantiation(self):
        """ test instantiation of BaseModel """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_BaseModel_instantiation_no_args(self):
        """ test instantiation of BaseModel with no args """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_BaseModel_instantiation_kwargs(self):
        """ test instantiation of BaseModel with kwargs """
        bm = BaseModel(name="Ronald")
        self.assertTrue(hasattr(bm, "name"))

if __name__ == "__main__":
    unittest.main()