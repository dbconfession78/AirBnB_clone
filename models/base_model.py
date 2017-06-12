#!/usr/bin/python3
"""
Module: base_model
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class"""

    dt_format = "%Y-%m-%dT%H:%M:%S.%f"  # move back to global after test

    def __init__(self, *args, **kwargs):
        """
        BaseModel initializer
        - if k/w args passed in, set class dict to args
        - if k/w args not passed in, set new uuid and current time
        """
        if kwargs:
            if "created_at" in kwargs:
                self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())  # obj to str
            self.created_at = datetime.now()  # obj
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute
        `updated_at` with the current datetime
        """
        self.updated_at = datetime.now()  # as obj
        models.storage.save()

    def to_json(self):
        """
        - returns a dictionary containing all class instance keys/values
          + class name in key `__class__`.
        - This method will be the first piece of
          the serialization/deserialization process.
        """
        json = {}
        json["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                json[k] = v.isoformat()
            else:
                json[k] = v
        return json

    def __str__(self):
        """
        returns class, id and class attributes format for
        printing as string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, str(self.id),
                                     self.__dict__)
