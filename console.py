#!/usr/bin/python3
"""
Module for the BaseModel class.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB Clone project.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_eof(self, arg):
        """
        EOF command to exit the program.
        Usage: Ctrl+D
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line or a line with only spaces + ENTER.
        """
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
