#!/usr/bin/python3
"""Module: test_console"""
from unittest.mock import create_autospec
import unittest
from console import HBNBCommand
import sys


class TestConsole(unittest.TestCase):
    """TestConsole class"""
    def setUp(self):
        """setup mock stdin and stdout"""
        self.stdout = create_autospec(sys.stdout)
        self.stdin = create_autospec(sys.stdin)

    def create(self, server=None):
        """instantiate the console"""
        return HBNBCommand(stdin=self.stdin, stdout=self.stdout)

    def test_quit(self):
        """test quit"""
        console = self.create()
        expected = True
        got = console.do_quit("")
        self.assertEqual(expected, got)
