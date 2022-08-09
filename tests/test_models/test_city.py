#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
from models.base_model import BaseModel
import models


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(City.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """
        test instance of City
        """
        test = City()
        self.assertEqual(test.state_id, "")
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = City()
        self.assertEqual(type(test.name), str)
        self.assertEqual(type(test.state_id), str)


if __name__ == "__main__":
    unittest.main()
