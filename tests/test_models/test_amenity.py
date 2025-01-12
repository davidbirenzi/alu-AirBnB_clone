#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    def test_attributes(self):
        """Test default attributes of Amenity"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == "__main__":
    unittest.main()
