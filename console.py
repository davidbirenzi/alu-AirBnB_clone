#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB Clone project.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        Usage: Ctrl+D
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line + ENTER.
        """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
