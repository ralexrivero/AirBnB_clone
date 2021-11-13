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
                *args: variable length argument list
                **kwargs: (key - value) pair of attributes 
            """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs['updated_at'] = datetime.now()
            kwargs['created_at'] = datetime.now()


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
