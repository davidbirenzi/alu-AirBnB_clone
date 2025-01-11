#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage

# List of valid classes
classes = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF signal."""
        print()
        return True

def emptyline(self):
        """Override the default behavior to do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)
