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
        # Ex: $ create BaseModel
        # If the class name doesn't exist, print ** class doesn't exist **
        # If the class name is missing, print ** class name missing **
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
        # Ex: $ show BaseModel 1234-1234-1234.
        # If the instance doesn't exist for the id,
        #     print ** no instance found **
        # If the id is missing, print ** instance id missing **
        # If the class name doesn't exist, print ** class doesn't exist **
        # If the class name is missing, print ** class name missing **
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
        # Ex: $ destroy BaseModel 1234-1234-1234.
        # If instance doesn't exist for the id, print ** no instance found **
        # If the id is missing, print ** instance id missing **
        # If the class name doesn't exist, print ** class doesn't exist **
        # If the class name is missing, print ** class name missing **
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
        # Ex: $ all BaseModel or $ all.
        # If the class name doesn't exist, print ** class doesn't exist **
        store = storage.all()
        if name:
            if name in class_models:
                for k, v in store.items():
                    if type(v).__name__ == class_models[arg[0]].__name__:
                        # if name in k:
                        print(v)
            else:
                print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """- Updates instance based on class name+id by adding/updating attr
- changes saved into file.json)\n"""
        # Ex: $ update BaseModel 1234-1234-1234 email
        #     "aibnb@holbertonschool.com".
        # Usage: update <class name> <id> <attribute name> <attribute value>
        # Only one attribute can be updated at the time
        # If the instance doesn't exist for the id,
        #     print ** no instance found **
        # If the id is missing, print ** instance id missing **
        # If the class name doesn't exist, print ** class doesn't exist **
        # If the class name is missing, print ** class name missing **
        # If the attribute name is missing, print ** attribute name missing **
        # If the value for the attribute name doesn't exist, print
        #     ** value missing **
        # All other arguments should not be used
        # (Ex: $ update BaseModel 1234-1234-1234
        #    email "aibnb@holbertonschool.com" first_name
        #    "Betty" = $ update BaseModel 1234-1234-1234 email
        #    "aibnb@holbertonschool.com")
        args = args.split()
        store = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing")
            return
        if len(args) == 3:
            print("** attribute value missing **")
            return
        if args[0] not in class_models:
                print("** class doesn't exist **")
                return
        for k, v in store.items():
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
