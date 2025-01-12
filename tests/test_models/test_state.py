#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests the State class"""

    def test_instance_creation(self):
        """Test instance creation"""
        state = State()
        self.assertIsInstance(state, State)

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test if 'name' attribute exists and is empty"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
