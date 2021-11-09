#!/usr/bin/env python3
""" Class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherits BaseModel
        Public class attribute
            name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize Amenity """
        super().__init__(*args, **kwargs)