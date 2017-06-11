#!/usr/bin/python3
"""
Module: user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        inherits BaseModel initialization
        """
        super().__init__(*args, **kwargs)
