#!/usr/bin/python3
from models.base_model import BaseModel

"""
This module defines the Place class.
"""

class Place(BaseModel):
    """Definition for the Place class."""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0  # There's a typo here; it should be "longitude" instead of "longtude."
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Constructor method for the Place class."""
        super().__init__(self, *args, **kwargs)
