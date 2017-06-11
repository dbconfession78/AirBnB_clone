#!/usr/bin/python3
"""
Module: state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        inherits BaseModel initialization
        """
        super().__init__(*args, **kwargs)
