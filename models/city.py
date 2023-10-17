#!/usr/bin/python3
from models.base_model import BaseModel

"""
This module defines the City class.
"""

class City(BaseModel):
    """Definition for the City class."""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Constructor method for the City class."""
        super().__init__(self, *args, **kwargs)
