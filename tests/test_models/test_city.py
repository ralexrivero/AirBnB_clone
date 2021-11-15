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

    def test_init(self):
        """ checks if it has the correct attributes """
        my_city = City()
        self.assertTrue(isinstance(my_city, City))
        self.assertTrue(isinstance(my_city.id, str))
        self.assertTrue(isinstance(my_city.created_at, str))
        self.assertTrue(isinstance(my_city.updated_at, str))
        self.assertTrue(isinstance(my_city.state_id, str))
        self.assertTrue(isinstance(my_city.name, str))

if __name__ == "__main__":
    unittest.main()