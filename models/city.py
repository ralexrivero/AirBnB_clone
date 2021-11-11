#!/usr/bin/env python3
""" class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits BaseModel
        Public class attribute
            state_id: string - empty string: it will be the State.id
            name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City """
        super().__init__(*args, **kwargs)