#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    def test_instance_creation(self):
        """Test instance creation"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test if 'name' attribute exists and is empty"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
