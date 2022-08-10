#!/usr/bin/python3
""" test Class Amenity """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel, Base
import models


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(Amenity, Base))

    def test_instance(self):
        """
        test instance of state
        """
        test = Amenity()
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(Amenity, Base))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = Amenity()
        self.assertEqual(type(test.name), str)

    def test_save_Amenity(self):
        """test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
