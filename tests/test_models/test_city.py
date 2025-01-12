#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def test_attributes(self):
        """Test default attributes of City"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == "__main__":
    unittest.main()
