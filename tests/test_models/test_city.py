#!/usr/bin/env python3
"""
unittests for the City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for City class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ checks if it has the correct attributes """
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)

if __name__ == "__main__":
    unittest.main()