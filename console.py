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
                   "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}
    # my_classes is a diccionary with the classes
    show_list = []
        for items in my_classes:
            show_list.append(items)
    instances = ["do_show", "do_destroy", "do_all", "do_update"] 

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
                len(args) > 0 and args[0] in HBNBCommand.my_classes
                new_object = HBNBCommand.my_classes[args[0]]()
                new_object.save()
                print(new_object.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
 
    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        """
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
