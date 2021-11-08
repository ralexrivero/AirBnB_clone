#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""
from models import *
import os
import sys
import json
import cmd
""" 6. Console 0.0.1 """


class HBNBCommand(cmd.Cmd):
    """consola HBNB"""

    prompt = "(hbnb) "
    my_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place}
    # my_classes is a diccionary with the classes

    def do_quit(self, args):
        """Quit command to exit the program"""

        quit()

    def do_EOF(self, args):
        """End Of File command to exit the program"""

        quit()
    
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""

        if not args:
            print("** class name missing **")
            return

        args = args.split() # divides a args into a list
        if len.args == 0:
            print("** class name missing **")
            return
        else:
            if len(args) > 0 and args[0] not in HBNBCommand.my_classes:
                print("** class doesn't exist **")
            else:
                len(args) > 0 and args[0] in HBNBCommand.my_classes:
                    new_object = HBNBCommand.my_classes[args[0]]()
                    new_object.save()
                    print(new_object.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
