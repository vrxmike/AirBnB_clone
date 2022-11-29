#!/usr/bin/python3
"""Unittest cases for models/city.py."""

import inittest
from datetime import datetime
import time
from models.city import City
import re
import pep8
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Restarts tests."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage.__FileStorage__objects = {}
        if os.path.isfile(FileStorage.__FileStorage__file_path):
            os.remove(FileStorage.__FileStorage__file_path)

    def test_pep8_base_model(self):
        """Test for PEP8 ok."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_pep8_tests_base(self):
        """Test for PEP8 ok."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
                ['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Checks if docstring exists."""
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_args(self):
        """Arguments o the instance"""
        b = City(8)
        self.assertEqual(type(b).__name__, "City")
        self.assertFalse(hasattr(b, "8"))
