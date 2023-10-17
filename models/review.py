#!/usr/bin/python3
from models.base_model import BaseModel

"""
This module defines the Review class.
"""

class Review(BaseModel):
    """Definition for the Review class."""
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """Constructor method for the Review class."""
        super().__init__(self, *args, **kwargs)
