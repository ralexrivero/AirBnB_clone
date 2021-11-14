#!/usr/bin/env python3

import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """ unittests for User class """
    def test_inherit(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """ checks if it has attributes """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

if __name__ == '__main__':
    unittest.main()