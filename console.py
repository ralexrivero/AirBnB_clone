#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import sys
import json
import cmd
import shlex
""" 6. Console 0.0.1 """

my_classes = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """-HBNBCommand(cmd.Cmd) is a class that inherits from cmd.Cmd
                    cmd.Cmd is methods to execute a command prompt command
                    line interface for a Python program.
       -prompt is a interpreter-specific string that is displayed to the user
       when they are ready to enter a command.
       -classes is a list of all the classes that inherit from BaseModel.
       -my_objects is a dictionary of all the instances of the classes
       in classes.
       -my_classes oa diccionary whit the classes.
       -storage is an instance of FileStorage.
       -self is an instance of HBNBCommand to use the methods of the class.
       -args is a list of arguments passed to the command.
       -args_list is a list of arguments passed to the command."""

    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]
    # my_classes is a diccionary with the classes
    # classes is a list with the classes

    show_list = []
    for items in my_classes:
        show_list.append(items)
    instances = ["do_show", "do_destroy", "do_all", "do_update"]

    def do_quit(self, args):
        """Quit command to exit the program.\n"""

        quit()

    def do_EOF(self, args):
        """End Of File command to exit the program\n"""

        quit()

    def emptyline(self):
        """Do nothing on empty line\n"""

        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.\n"""

        if not args:
            print("** class name missing **")
            return
        args_list = shlex.split(args)
        """shlex is a lexical analyser for simple shell-like syntax;
           and shlex.split() splits a string into a list of tokens."""
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """Prints the string representation of an instance, format:
        show <class name> <id>.\n"""

        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
              shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in my_classes:
            print("** class doesn't exist **")
        else:
            if len(args_list) == 1:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id.\n"""

        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
                shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if len(args_list) == 0:
            print("** class name missing **")
            return
        elif args_list[0]in my_classes:
            """if the args_list[0] is in my_classes, then the class exists"""
            if len(args_list) > 1:
                """if the lenght of args_list is greater than 1,
                then the id is passed"""
                key = args_list[0] + "." + args_list[1]
                """key = args_list[0] + "." + args_list[1]
                    key is the key to search in the dictionary"""
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    """pop(key) removes the key from the dictionary"""
                    models.storage.save()
                    """save() saves the changes in the JSON file"""
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name.\n"""

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).\n"""


if __name__ == "__main__":
    """__name__ is a special variable that holds the name of the current
    module and __main__ is the name of the "main" module; if this module
    is being run as the main module, __name__ will be __main__."""
    HBNBCommand().cmdloop()
    """cmdloop() is a method that runs a command prompt command line interface
    for a Python program."""
