#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""

import os
import sys
import json
import cmd
""" 6. Console 0.0.1 """

class HBNBCommand(cmd.Cmd):
    """consola HBNB"""

    prompt = "(hbnb) "

def do_quit(self, arg):
    """Quit command to exit the program"""
    quit()

def do_EOF(self, arg):
    """EOF command to exit the program"""
    quit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()