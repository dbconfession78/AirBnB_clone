#!/usr/bin/python3
"""
Module: console
"""
import cmd
from models import storage, class_models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    console class used to interface with HBNB
    """

    def do_EOF(self, line):
        """(ctrl+d) command to halt process and exit console\n"""
        print()
        return True

    def do_quit(self, line):
        """command to exit console\n"""
        return True

    def emptyline(self):
        """Called when empty line is passed to the prompt\n"""
        pass

    def do_create(self, class_model):
        """creates a new instance of BaseModel and saves to file\n"""
        if class_model in class_models:
            new_object = class_models[class_model]()
            new_object.save()
            print(new_object.id)
        elif len(class_model) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints instance in str format based on id and class name\n"""
        store = storage.all()
        args = [x.strip() for x in args.split()]
        if len(args) == 2:
            if args[0] not in class_models:
                print("** class doesn't exist **")
            else:
                instance_key = args[0] + "." + args[1]
                try:
                    print(store[instance_key])
                except:
                    print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes instance based on class name+id (changes saved to file.json)
"""
        store = storage.all()
        args = [x.strip() for x in args.split()]
        if len(args) == 2:
            if args[0] not in class_models:
                print("** class doesn't exist **")
            else:
                instance_key = args[0] + "." + args[1]
                try:
                    del(storage.all()[instance_key])
                    storage.save()
                except:
                    print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, name=""):
        """Prints string repr. of all instances based on class name\n"""
        store = storage.all()
        count = 0
        if name:
            if name in class_models:
                for k, v in store.items():
                    if name in k:
                        print(v)
                        count += 1
                if count == 0:
                    print("[]")
            else:
                print("** class doesn't exist **")
        else:
            for k, v in store.items():
                print(v)

    def do_update(self, args):
        """- Updates instance based on class name+id by adding/updating attr
- changes saved into file.json)\n"""
        args = args.split()
        store = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in class_models:
                print("** class doesn't exist **")
                return
        for k, v in store.items():
            if args[3].startswith('"') and args[3].endswith('"'):
                args[3] = args[3][1:-1]
            instance_key = args[0] + "." + args[1]
            if k == instance_key:
                setattr(v, args[2], args[3])
                storage.save()
                return
        print("** no instance found **")

if __name__ == "__main__":
    console = HBNBCommand()
    console.prompt = "(hbnb) "
    console.cmdloop()
