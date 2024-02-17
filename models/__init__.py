#!/usr/bin/python3
"""change storage type directly by using an environment variable"""
from os import getenv

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
