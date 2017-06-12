#!/usr/bin/python3
"""Module: test_console"""
import unittest
import models
from console import HBNBCommand
from datetime import datetime
from models.base_model import BaseModel



class TestConsole(unittest.TestCase):
    """
    Console testing
    """
    console = HBNBCommand()
    def create(self):
        """ test create"""
        self.console = HBNBCommand()
        args = {'updated_at': datetime(2017, 6, 11, 10, 47, 00, 123456),
                'id': '6493e0f4-0251-4a20-93c0-339ea262fe0e',
                'created_at': datetime(2017, 6, 11, 17, 50, 16, 307880),
                'name': 'SELF_MODEL'}
        self.model = BaseModel(**args)
        self.model.save()

    def destroy(self):
        """ test destroy"""
        self.console.do_destroy(
            "BaseModel 6493e0f4-0251-4a20-93c0-339ea262fe0e")

    def test_quit(self):
        """test quit"""
        with self.assertRaises(SystemExit):
            self.console.do_quit(self.console)
