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
    __file_path = "./file.json"
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
        """method: reload - deserialize"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                r = json.load(f)
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.place import Place
            from models.amenity import Amenity
            from models.review import Review
            for i in r.keys():
                try:
                    r[i]['created_at'] = datetime.datetime.strptime(r[i]
                        ['created_at'], self.dt_format)
                    r[i]["updated_at"] = datetime.datetime.strptime(r[i]
                        ["updated_at"], self.dt_format)
                except:
                    pass
                if r[i]["__class__"] == "BaseModel":
                    self.__objects[i] = BaseModel(**r[i])
                elif r[i]["__class__"] == "User":
                    self.__objects[i] = User(**r[i])
                elif r[i]["__class__"] == "State":
                    self.__objects[i] = State(**r[i])
                elif r[i]["__class__"] == "City":
                    self.__objects[i] = City(**r[i])
                elif r[i]["__class__"] == "Place":
                    self.__objects[i] = Place(**r[i])
                elif r[i]["__class__"] == "Amenity":
                    self.__objects[i] = Amenity(**r[i])
                elif r[i]["__class__"] == "Review":
                    self.__objects[i] = Review(**r[i])
            return self.__objects
        else:
            return {}
