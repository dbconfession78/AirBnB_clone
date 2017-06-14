#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os
import json
"""Module: test_file_storage """


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""
    def setUp(self):
        """instantiate class"""
        self.cls = FileStorage()
        self.bm = BaseModel()

    def test_attrs(self):
        """testing the attributes of FileStorage"""
        self.assertFalse(hasattr(self.cls, "random_attr"))
        self.assertTrue(hasattr(self.cls, "class_models"))

    def test_instantiation(self):
        """ instatiate class """
        self.assertIsInstance(storage, FileStorage)

    def test_json_file(self):
        """file.json"""
        expected = True
        got = False
        os.remove("./file.json")
        self.bm.save()
        _id = self.bm.id
        with open("./file.json", mode="r", encoding="utf-8") as _file:
            load = json.load(_file)
        for key in load.keys():
            if _id in key:
                got = True
        self.assertTrue(expected, got)


    def test_to_json(self):
        """to_json() method"""
        expected = True
        got = True
        _json = self.bm.to_json()
        try:
            json.dumps(_json)
        except:
            got = False
        self.assertTrue(expected, got)

    def test_reload(self):
        """ reload() method"""
        expected = True
        got = False
        os.remove("./file.json")
        self.bm.save()
        _id = self.bm.id
        fs = FileStorage()
        fs.reload()
        all_dicts = fs.all()
        for key in all_dicts.keys():
            if _id in key:
                got = True
        self.assertTrue(expected, got)

    def test_save_and_reload(self):
        """save and reload object"""
        expected = True
        got = False
        os.remove("./file.json")
        self.bm.save()
        _id = self.bm.id
        fs = FileStorage()
        fs.reload()
        all_dicts = fs.all()
        for key, val in all_dicts.items():
            if _id in key:
                if type(val).__name__ == "BaseModel":
                    got = True
        self.assertTrue(expected, got)


    def test_module_doc(self):
        """ module documentation """
        expected = True
        got = len(self.cls.__doc__) > 0
        self.assertEqual(expected, got)

    def test_class_doc(self):
        """ class documentation """
        expected = True
        got = len(FileStorage.__doc__) > 0
        self.assertEqual(expected, got)

    def test_init_doc(self):
        """__init__() documentation"""
        expected = True
        got = len(FileStorage.__init__.__doc__) > 0
        self.assertEqual(expected, got)

    def test_all_doc(self):
        """ all() method documentation"""
        expected = True
        got = len(FileStorage.all.__doc__) > 0
        self.assertEqual(expected, got)

    def test_new_doc(self):
        """ new() method documentation """
        expected = True
        got = len(FileStorage.new.__doc__) > 0
        self.assertEqual(expected, got)

    def test_new_doc(self):
        """ save() method documentation """
        expected = True
        got = len(FileStorage.save.__doc__) > 0
        self.assertEqual(expected, got)

    def test_reload_doc(self):
        """ reload() method documentation """
        expected = True
        got = len(FileStorage.reload.__doc__) > 0
        self.assertEqual(expected, got)

if "__main__" == __name__:
    unittest.main()
