#!/usr/bin/python3
from models.base_model import BaseModel

"""
This module defines the State class.
"""

class State(BaseModel):
    """Definition for the State class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method for the State class."""
        super().__init__(self, *args, **kwargs)
