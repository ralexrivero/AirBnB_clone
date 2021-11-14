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
        filestorage = FileStorage()
        instances = filestorage.all
        self.assertIsInstance(instances, dict)
        self.assertEqual(len(instances), 0)
        self.assertIs(instances, filestorage._FileStorage__objects)
        self.assertIsNotNone(filestorage._FileStorage__file_path)

if __name__ == '__main__':
    unittest.main()