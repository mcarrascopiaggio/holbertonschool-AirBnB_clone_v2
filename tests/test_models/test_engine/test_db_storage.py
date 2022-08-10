#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.engine.db_storage import DBStorage


class test_dbStorage(unittest.TestCase):

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

