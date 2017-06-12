#!/usr/bin/python3
from models.base_model import BaseModel
"""module: class User"""


class User(BaseModel):
    '''class User'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''method: init'''
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
