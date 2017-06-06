#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    # must implement:
    # ``quit`` and ``EOF`` to exit the program
    # ``help``
    # custom prompt: ``(hbnb)``
    # empty line + ``ENTER`` shouldn't execute anything
    # code should not be executed when imported
    """
    console class used to interface with HBNB
    """

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

    """
    program initializer
       - sets (hbnb prompt)
    """
if __name__ == '__main__':
    console = HBNBCommand()
    console.prompt = "(hbnb) "
    console.cmdloop()
