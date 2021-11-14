#!/usr/bin/env python3
"""
Unitest for the FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):

    def test_all_FS(self):
        """
        Test the all function
        """
       
        self.assertEqual(FileStorage, type(FileStorage()))
        

if __name__ == '__main__':
    unittest.main()