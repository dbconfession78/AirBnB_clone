#!/usr/bin/python3
"""
Module: city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes instance of City"""
        super().__init__(*args, **kwargs)
