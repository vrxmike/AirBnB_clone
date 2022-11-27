#!/usr/bin/pyhton3
"""This module creates a Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
