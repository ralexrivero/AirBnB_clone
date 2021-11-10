#!/usr/bin/python3
""" Class FileStorage
"""

import json
from os import read
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}
class FileStorage:
    """ Class FileStorage"""
    
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """init method"""
        self.__reload()

    def all(self):
        """all method"""
        return FileStorage.__objects

    def new(self, obj):
        """new method"""
        if new_obj is None:
            for new_obj in FileStorage.__objects:
                FileStorage.__objects[new_obj] = obj

    def save(self):
        """save method"""
        dict = {}
        for i in FileStorage.__objects.keys():
            dict[i] = FileStorage.__objects[i].to_json()
        with open(self.__file_path, 'w') as file:
            json.dump(dict, file)
 
   def reload(self):
        """reload method"""
        try:
            with open(self.__file_path, 'r') as file:
                jeison = json.load(file)
            for i in jeison:
                self.__objects[i] = classes[jeison[i]["__class__"]](**jeison[i])
        except:
            pass