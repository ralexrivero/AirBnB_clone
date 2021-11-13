#!/usr/bin/env python3
""" BaseModel that defines all common attributes/methods for other classes """
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """ instantiates a new object
            Args:
                *args: unused
                **kwargs: (key - value) pair of attributes 
            """

        if len(args) > 0:
            for i in args[0]:
                setattr(self, i, args[0][i])
                """setattr is a function that takes two arguments:
                the name of the attribute to be set and the value to be
                assigned to it.
                """
        else:
            self.created_at = datetime.now()
            self.id = str(uuid4())

        for i in kwargs:
            print("kwargs: {}: {}".format(i, kwargs[i]))

    def __str__(self):
        """ Returns a string representation of the object """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute
        updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
