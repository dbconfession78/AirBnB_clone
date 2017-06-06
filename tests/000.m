Class: HBNBCommand
==================

Import class
------------
	>>> HBNBCommand  = __import__("console").HBNBCommand
        >>> import unittest

Check for documentation
-----------------------
	>>> print(len(HBNBCommand.__doc__) > 0)
	True

	>>> console = HBNBCommand()
	...

	>>> console = HBNBCommand()
	>>> console.prompt = "(hbnb)"
	>>> console.cmdloop(console)
	(hbnb)
