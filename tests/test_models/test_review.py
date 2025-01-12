#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests the Review class"""

    def test_attributes(self):
        """Test default attributes of Review"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == "__main__":
    unittest.main()
