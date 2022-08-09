#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import models
from models.base_model import BaseModel, Base


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
        
    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(User.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """
        test instance of User
        """
        test = User()
        self.assertEqual(test.email, "")
        self.assertEqual(test.password, "")
        self.assertEqual(test.first_name, "")
        self.assertEqual(test.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
