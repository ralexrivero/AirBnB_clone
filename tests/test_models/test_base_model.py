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

###############################################################################
# test_BaseModel_instantiation
###############################################################################

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

    def test_BaseModel_instantiation_store_object(self):
        """test stored objects"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_BaseModel_created_date(self):
        """ test created_at """
        bm = BaseModel()
        self.assertTrue(isinstance(bm.created_at, datetime))

    def test_BaseModel_created_date2(self):
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime)

    def test_BaseModel_updated_date(self):
        """ test updated_at """
        bm = BaseModel()
        self.assertTrue(isinstance(bm.updated_at, datetime))

    def test_BaseModel_updated_date2(self):
        bm = BaseModel()
        self.assertEqual(type(bm.updated_at), datetime)

    def test_BaseModel_create_sleep(self):
        """ create two objects at different time """
        bm1 = BaseModel()
        sleep(1)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

###############################################################################
# test_BaseModel_str
###############################################################################

    def test_BaseModel_str(self):
        """ test str method """
        bm = BaseModel()
        self.assertEqual(type(str(bm)), str)

if __name__ == "__main__":
    unittest.main()