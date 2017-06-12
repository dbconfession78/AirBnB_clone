#!/usr/bin/python3
"""Module: user"""
from models.base_model import BaseModel


class User(BaseModel):
    """eUser class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes intance of User"""
        super().__init__(self, *args, **kwargs)
