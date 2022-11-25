#!/usr/bin/python3
"""Defines the state class."""
from models.base_moel import BaseModel


class State(BaseModel):
    """Represent a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""
