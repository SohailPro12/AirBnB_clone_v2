#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()

    def assert_output(self, expected_output, function, *args):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            function(*args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_help_quit(self):
        self.assert_output("Exits the program with formatting", self.cmd.help_quit)

    def test_help_EOF(self):
        self.assert_output("Exits the program without formatting", self.cmd.help_EOF)

    def test_help_create(self):
        self.assert_output("Creates a class of any type\n[Usage]: create <className>", self.cmd.help_create)

    def test_help_show(self):
        self.assert_output("Shows an individual instance of a class\n[Usage]: show <className> <objectId>", self.cmd.help_show)

    def test_help_destroy(self):
        self.assert_output("Destroys an individual instance of a class\n[Usage]: destroy <className> <objectId>", self.cmd.help_destroy)

    def test_help_all(self):
        self.assert_output("Shows all objects, or all of a class\n[Usage]: all <className>", self.cmd.help_all)

    def test_help_count(self):
        self.assert_output("Usage: count <class_name>", self.cmd.help_count)

    def test_help_update(self):
        self.assert_output("Updates an object with new information\nUsage: update <className> <id> <attName> <attVal>", self.cmd.help_update)

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_create("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output != "")
            self.assertIsInstance(BaseModel().id, str)

    def test_do_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_show("BaseModel 1234-5678")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            user_instance = User()
            user_instance.id = "1234-5678"
            self.cmd.do_show("User 1234-5678")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(user_instance) in output)

    def test_do_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_destroy("BaseModel 1234-5678")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            user_instance = User()
            user_instance.id = "1234-5678"
            self.cmd.do_destroy("User 1234-5678")
            self.assertTrue("1234-5678" not in self.cmd.classes["User"].__dict__)

    def test_do_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_all("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")

            user_instance = User()
            self.cmd.do_all("User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(user_instance) in output)

    def test_do_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_count("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "0")

            user_instance = User()
            self.cmd.do_count("User")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "1")

    def test_do_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_update("BaseModel 1234-5678 name John")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            user_instance = User()
            user_instance.id = "1234-5678"
            self.cmd.do_update("User 1234-5678 name John")
            self.assertEqual(user_instance.name, "John")

if __name__ == '__main__':
    unittest.main()

