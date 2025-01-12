#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def test_instance_creation(self):
        """Test instance creation"""
        city = City()
        self.assertIsInstance(city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test if 'state_id' and 'name' attributes exist and are empty"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
