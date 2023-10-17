#!/usr/bin/python3

"""
This module defines the User class.
"""

from models.base_model import BaseModel
import json

class User(BaseModel):
    """
    Base model class for User objects.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
