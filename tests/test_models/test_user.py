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

    def test_types(self):
        """ checks if it has correct types """
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_values(self):
        """ checks if it has correct values """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """ checks if it has correct string representation """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_save(self):
        """ checks if it saves correctly """
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict(self):
        """ checks if it returns correct dictionary """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertTrue("__class__" in user_dict)
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)
        self.assertTrue("id" in user_dict)
        self.assertTrue("email" in user_dict)
        self.assertTrue("password" in user_dict)
        self.assertTrue("first_name" in user_dict)
        self.assertTrue("last_name" in user_dict)

if __name__ == '__main__':
    unittest.main()