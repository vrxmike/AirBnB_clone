#!/usr/bin/python3
"""Unittest module for the review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
import models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Test Cases for the Review class.""""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down the test methods."""
        self.resetStorage()
        pass

    def test_resetStorage(self):
        """Resets FileStorage data."""
        FileStorage.__FileStoarage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
