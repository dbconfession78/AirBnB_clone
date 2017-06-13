#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """instantiates new instance of State"""
        super().__init__(*args, **kwargs)
