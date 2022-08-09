#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import models
from models.base_model import BaseModel, Base


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


if __name__ == "__main__":
    unittest.main()
