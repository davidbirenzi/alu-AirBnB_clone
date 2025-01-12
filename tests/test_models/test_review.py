#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests the Review class"""

    def test_instance_creation(self):
        """Test instance creation"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test if 'place_id', 'user_id', and 'text' attributes exist and are empty"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
