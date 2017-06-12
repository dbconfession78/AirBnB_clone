#!/usr/bin/python3
"""
Module: __init__
initializer for the `models` module
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place



storage = FileStorage()
storage.reload()
