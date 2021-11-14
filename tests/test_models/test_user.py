#!/usr/bin/env python3

import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """ unittests for User class """
    def test_inherit(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))