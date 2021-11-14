#!/usr/bin/env python3
"""
Unitest for models/state.py

Unittest classes:
    test_state_instantiates
    test_state_save
    test_state_dict
    """

import unittest
import models
from models.state import State


class test_state_instantiates(unittest.TestCase):
    """ Unittest for testing instantiation"""

    def test_instantiation(self):
        self.assertIs(State, type(State()))

    def test_instantiation_with_kwargs(self):
        self.assertIs(State, type(State(name="California")))


if __name__ == "__main__":
    unittest.main()
