#!/usr/bin/python3
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime

"""
Module consule.py a cmd console
"""


class HBNBCommand(cmd.Cmd):
    ''' Console module for object interaction via command line. '''
    prompt = "(hbnb)"

    All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_EOF(self, arg):
        '''Handle program exit when Ctrl+D is pressed.'''
        print("")
        return True

    def do_quit(self, arg):
        ''' Exit the program gracefully. '''
        return True

    def do_nothing(self, arg):
        ''' Placeholder method to handle empty lines. '''
        pass

    def emptyline(self):
        ''' Handle empty line + Enter key. '''
        pass

    def do_create(self, args):
        ''' Create an instance and print its ID. '''
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

    def do_show(self, args):
        ''' Display an instance based on class name and ID. '''
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            print(str(obj[obj_key]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        ''' Delete an instance based on class name and ID. '''

        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            del obj[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        ''' List all instances based on class name or all classes. '''
        storage.reload()
        json_dict = []
        obj_dict = storage.all()
        if args == "":
            for key, value in obj_dict.items():
                json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        arg = shlex.split(args)
        if arg[0] in HBNBCommand.All_class_dict.keys():
            for key, value in obj_dict.items():
                if arg[0] in key:
                    json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        ''' Update an instance's attribute based on class name and ID. '''

        if not args:
            print("** class name missing **")
            return
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(arg) == 2):
            print("** attribute name missing **")
            return
        if (len(arg) == 3):
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if arg[2] in obj_dict.keys():
            d_type = type(obj_dict[arg[2]])
            print(d_type)
            obj_dict[arg[2]] = type(obj_dict[arg[2]])(arg[3])
        else:
            obj_dict[arg[2]] = arg[3]
        storage.save()

    def do_update2(self, args):
        ''' Update an instance's attributes from a dictionary representation. '''

        if not args:
            print("** class name missing **")
            return
        my_dict = "{" + args.split("{")[1]
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dict == "{"):
            print("** attribute name missing **")
            return
        my_dict = my_dict.replace("\'", "\"")
        my_dict = json.loads(my_dict)
        obj_inst = obj[obj_key]
        for k in my_dict:
            if hasattr(obj_inst, k):
                d_type = type(getattr(obj_inst, k))
                setattr(obj_inst, k, my_dict[k])
            else:
                setattr(obj_inst, k, my_dict[k])
        storage.save()

    def do_count(self, args):
        ''' Count the number of instances for a class. '''
        obj = storage.all()
        cnt = 0
        for key in obj:
            if (args in key):
                cnt += 1
        print(cnt)

    def default(self, args):
        ''' Handle custom object commands in the format {<>}.all(), {<>}.count()
        {<>}.show(), {<>}.destroy(), {<>}.update()'''
        cmd_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        arg = args.strip()
        val = arg.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = val[0]
        command = val[1].split("(")[0]
        line = ""
        if (command == "update" and val[1].split("(")[1][-2] == "}"):
            inputs = val[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = val[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in cmd_dict.keys()):
            cmd_dict[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
