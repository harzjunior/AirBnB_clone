#!/usr/bin/python3
from models.base_model import BaseModel

"""Defines the Amenity class."""

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method for the Amenity class."""
        super().__init__(self, *args, **kwargs)
