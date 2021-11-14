#!/usr/bin/env python
"""
Unitest for models/amenity.py

Unittest classes:
    Test_amentity_instantiation
    """
import os
import unittest
import models
from datetime import datetime
from models.amenity import Amenity


class Test_models_amenity(unittest.TestCase):
    """
        Test_models_amenity class
    """

    def setUp(self):
        """
        Set up
        """
        self.amenity = Amenity()

    def test_instantiation(self):
        """
        Test instantiation
        """
