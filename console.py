#!/usr/bin/python
"""
Console for AirBnB project.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Console for AirBnB project
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self, arg):
        """
        Handle the help_quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handle the EOF (end-of-file) signal.
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
