#!/usr/bin/python3
from mymodule import MyCLI
from unittest.mock import create_autospec
import console

HBNBCommand = console.HBNBCommand
test = __import__("console").test

class TestConsole(unittest.TestCase):
    def test_code_not_run_on_import(self):
        self.assertEqual(print((__import__("console").HBNBCommand)) == print("<class 'console.HBNBCommand'>"), True)
if __name__ == '__main__':
    unittest.main()
