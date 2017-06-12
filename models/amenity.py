#!/usr/bin/python3
"""
Module: amenity
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize instqance of Amenity"""
        super().__init__(*args, **kwargs)
