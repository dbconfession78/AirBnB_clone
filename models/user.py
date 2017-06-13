#!/usr/bin/python3
"""Module: class User"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initializes new instance of User"""
        super().__init__(*args, **kwargs)
