#!/usr/bin/python3
"""
Module: file_storage
"""
import json
import sys
import os.path
from datetime import datetime

dt_format = "%Y-%m-%dT%H:%M:%S.%f"


class FileStorage:
    """
    handles file storage operations
    - save: converts obj dict to JSON and writes to file
    - load: reads file and converts JSON to object dict
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns all object instances
        """
        return self.__objects

    def new(self, obj):
        """
        adds new object instance to objects
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        store = {}
        for k, v in self.__objects.items():
            store[k] = v.to_json()
        with open(self.__file_path, mode="w", encoding="utf-8") as _file:
            json.dump(store, _file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only
        if the JSON file exists ; otherwise, do nothing)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as _file:
                loaded = json.load(_file)

                for _id in loaded.keys():
                    try:
                        loaded[_id]["created_at"] = datetime.strptime(
                            loaded[_id]["created_at"], dt_format)  # str -> obj
                        loaded[_id]["updated_at"] = datetime.strptime(
                            loaded[_id]["updated_at"], dt_format)  # str -> obj
                    except:
                        print("Error: Unable to deserialize created and/or\
                        updated updated time")
                        sys.exit(-1)
                    from models.base_model import BaseModel
                    self.__objects[_id] = BaseModel(**loaded[_id])

        return self.__objects
