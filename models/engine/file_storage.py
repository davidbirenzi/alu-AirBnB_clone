"""Defines a class for serializing and deserializing JSON files."""
import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path )"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key, value in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                objects = json.load(file)
                for key, value in objects.items():
                    class_name = value["__class__"]
                    if class_name == "User":
                        FileStorage.__objects[key] = User(**value)
        else:
            pass
