#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import unittest
from models.base_model import BaseModel
import models
from os import getenv
import pep8


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except as exception:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "skip if db")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_documentation(self):
        """
        Test if there is documentation
        """
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)

    def test_id_assignment(self):
        """
        Test assignment of UUID is of type string and len is equal to 36
        A UUID is made up of hex digits  (4 chars each) along with 4 “-”
        symbols, which make its length equal to 36 characters.
        """
        test = BaseModel()
        self.assertIsInstance(test.id, str)
        self.assertEqual(len(test.id), 36)

    def test_instance_of_BaseModel(self):
        """
        Test instantiation of a BaseModel class
        """
        test = BaseModel()
        self.assertEqual(type(test), BaseModel)
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))

    def test_instance_with_kwarg(self):
        """
        Test instantation with kwarg
        """
        test = BaseModel(name="Marce y Juanma")
        self.assertTrue(hasattr(test, "name"))

    def test_created_at(self):
        """
        Test that when creating an instance of BaseModel "datetime" is assigned
        correctly to the public instance attribute: "created_at" and is of type
        "datetime".
        Use of function "hasattr" to check if the attribute was created as it
        should be.
        """
        test = BaseModel()
        self.assertTrue(hasattr(test, "created_at"))
        self.assertEqual(type(test.created_at), datetime)

    def test_updated_at(self):
        """
        Test that when creating an instance of BaseModel "datetime" is assigned
        correctly to the public instance attribute: "updated_at" and is of type
        "datetime".
        Use of function "hasattr" to check if the attribute was created as it
        should be.
        """
        test = BaseModel()
        self.assertTrue(hasattr(test, "updated_at"))
        self.assertEqual(type(test.updated_at), datetime)

    def test_save(self):
        """
        Test save model: storage created time and updated time
        """
        test = BaseModel()
        test.save()
        self.assertNotEqual(test.created_at, test.updated_at)

    def test_to_dict(self):
        """
        test to dict method
        """
        test = BaseModel()
        test_dict = test.to_dict()
        self.assertIsInstance(test_dict, dict)

    def test_format_date(self):
        """
        test date format
        """
        obj = BaseModel()
        dic = obj.to_dict()
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)

    def test_date(self):
        """test date"""
        obj1 = BaseModel()
        self.assertEqual(obj1.created_at, obj1.updated_at)

    def test_pep8_base_model(self):
        """Pep8 base_model.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')


if __name__ == '__main__':
    unittest.main()
