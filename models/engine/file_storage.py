#!/usr/bin/python3
"""
Module: file_storage
"""
import json
import sys
import os.path
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

dt_format = "%Y-%m-%dT%H:%M:%S.%f"


class FileStorage:
    """
    handles file storage operations
    - save: converts obj dict to JSON and writes to file
    - load: reads file and converts JSON to object dict
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.__class_models = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
        }

    def all(self):
        """
        returns all object instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        adds new object instance to objects
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        store = {}
        for k, v in FileStorage.__objects.items():
            store[k] = v.to_json()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as _file:
            json.dump(store, _file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only
        if the JSON file exists ; otherwise, do nothing)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            for _id, v in loaded.items():

                try:
                    loaded[_id]["created_at"] = datetime.strptime(
                    loaded[_id]["created_at"], dt_format)
                    loaded[_id]["updated_at"] = datetime.strptime(
                        loaded[_id]["updated_at"], dt_format)
                except:
                    pass
 #                   print("Error: unable to deserialize current and/or\
 #updated time")
  #                  exit(-1)
                cls = loaded[_id].pop("__class__", None)
                FileStorage.__objects[_id] = self.__class_models[cls](**v)
