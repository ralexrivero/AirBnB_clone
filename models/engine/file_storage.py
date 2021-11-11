#!/usr/bin/env python3
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
    """__file_path is the path of the json file"""
    __objects = {}
    """__objects is a dictionnary of all objects"""

    def __init__(self):
        """constructor metod of FileStorage class, initialize all
        the class attributes"""

    def all(self):
        """Reeturn dictionnary of all objects"""
        return FileStorage.__objects
        """return a dictionnary of all objects"""

    def new(self, obj):
        """add object to the dictionnary __objects"""
        if obj is None:
            for new_obj in FileStorage.__objects:
                """this for loop utilise a new_obj to run
                    the loop for each object in the dictionnary"""
                FileStorage.__objects[new_obj] = obj

    def save(self):
        """serialize and save objects from __objects to a file
        in json in format json"""
        dictionary = {}
        """dicttionary is an empty dictionnary"""
        for key, value in FileStorage.__objects.items():
            """this for loop utilise a key and valiu to run
            FileStorage.__objects.items() and create a dictioanry of
            key and value"""
            dictionary[key] = value.to_dict()
        """dict[key] is equal to value.__dict__"""
        with open(self.__file_path, 'w') as f:
            """open(self.__file_path, 'w') open the json file in write mode"""
            json.dump(dictionary, f)
            """dump(dictionary, f) dump the dictionnary in the file f"""

    def reload(self):
        """deserialize and lode objects from the file into python
        objects to dictionary __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                """open( self.__file_path, 'r') open the json file
                in read mode"""
                my_dict = json.load(f.read)
                """load(f.read) load the file f and read it"""
            for key, value in my_dict.items():
                """this for loop utilise a key and valiu to run
                    my_dict.items() and create a dictioanry of key and value"""
                new_object = key.split('.')[0]
                """new_object is equal to key.split('.')[0]
                    this split the key and take the first part of the key"""
                if new_object in classes:
                    self.__objects[key] = classes[new_object](**value)
                    """this if statement is used to create a new object
                        with the class name of new_object and its value"""
        except:
            pass
        """except is used to catch the error if the file is empty"""
