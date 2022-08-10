#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.engine.db_storage import DBStorage
import pep8


class test_dbStorage(unittest.TestCase):

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_pep8_db_storage(self):
        """Pep8 db_storage.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')


if __name__ == "__main__":
    unittest.main()
