#!/usr/bin/python3
"""
Module: base_model
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class"""

    dt_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """initializes new instance of BaseModel"""
        if kwargs:
            kwargs = self.sanitize_deserialization(kwargs)
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())  # obj -> str
            self.created_at = datetime.now()  # as obj
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute
        `updated_at` with the current datetime
        """
        self.updated_at = datetime.now()  # as obj
        models.storage.save()

    def to_json(self):
        """returns objects converted to JSON format"""
        json = {}
        json["__class__"] = type(self).__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                json[k] = v.isoformat()
            else:
                json[k] = v
        return json

    def sanitize_deserialization(self, kwargs):
        """deserializes datetime attributes if necessary"""
        if not isinstance(kwargs["created_at"], datetime):
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], self.dt_format)

        if "updated_at" in kwargs:
            if not isinstance(kwargs["updated_at"], datetime):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], self.dt_format)
        return kwargs

    def __str__(self):
        """
        returns class, id and class attributes format for
        printing as string
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)
