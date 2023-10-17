#!/usr/bin/python3
import os.path
import json
import os

"""
This module, file_storage,
contains a class called FileStorage.
FileStorage handles the serialization of instances
to a JSON file and the deserialization of a JSON file back into instances.
"""

class FileStorage():
    """
    FileStorage is responsible for serializing instances to a JSON file and deserializing a JSON file to recreate instances.
    """
    ''' initializing values '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        The `all` method returns the dictionary of stored objects (__objects).
        '''
        return self.__objects

    def new(self, obj):
        '''
        The `new` method adds an object to the __objects dictionary, using the object's class name and id as the key.
        '''
        if obj:
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        '''
        The `save` method serializes the objects in __objects and stores them in a JSON file specified by the __file_path.
        '''
        my_dict = {}

        for keys, val in self.__objects.items():
            '''
            This block serializes each object using its key.
            '''
            my_dict[keys] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        '''
        The `reload` method deserializes and loads objects from a JSON file into the __objects dictionary.
        '''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])
