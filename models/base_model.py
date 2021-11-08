#!/usr/bin/env python3
""" BaseModel that defines all common attributes/methods for other classes """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel
            Args:
                *args: 
                **kwargs: key - value pairs
        """
    