#!/usr/bin/python3
"""Unittest cases for place"""

import unittest
from models.place import Place
import pep8
import os
import re
import json
import time
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """Class Place -Unittest """

    def test_setUp(self):
        """SetsUps tests"""
        pass

    def test_tearDown(self):
        """Restart tests"""
        self.resetStorage()
        pass

    def test_resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Place class."""

        b = Place()
        self.asertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assetIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests teh attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
