#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import models
from models.base_model import BaseModel, Base
import pep8


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(State.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """
        test instance of state
        """
        test = State()
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = State()
        self.assertEqual(type(test.name), str)

    def test_pep8_state(self):
        """Pep8 state.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/state.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')


if __name__ == "__main__":
    unittest.main()
