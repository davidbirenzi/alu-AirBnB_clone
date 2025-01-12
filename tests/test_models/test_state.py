#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Tests the State class"""

    def test_attributes(self):
        """Tests the attributes of the State class"""
        state = State()
        self.assertEqual(state.name, "")
