#!/usr/bin/python3
""" testing for BaseModel class
    documentation and behavior
"""

from datetime import datetime
import inspect
import models
import pycodestyle
import unittest
from unittest import mock

BaseModel = models.base_model.BaseModel
docs = models.base_model.__doc__


class BaseModelDoc(unittest.TestCase):
    """Check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Basic set"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def pep8(self):
        """models/base_model.py apply to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_docstring(self):
        """If is present module docstring"""
        self.assertIsNot(docs, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(docs) > 1,
                        "base_model.py needs a docstring")

    def test_docstring_class(self):
        """BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_docstring_fun(self):
        """Docstring in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )
