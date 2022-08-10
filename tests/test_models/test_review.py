#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import models
from models.base_model import BaseModel, Base
import pep8


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(Review.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """
        test instance of state
        """
        test = Review()
        self.assertEqual(test.place_id, "")
        self.assertEqual(test.user_id, "")
        self.assertEqual(test.text, "")
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = Review()
        self.assertEqual(type(test.place_id), str)
        self.assertEqual(type(test.user_id), str)
        self.assertEqual(type(test.text), str)

    def test_pep8_review(self):
        """Pep8 review.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')


if __name__ == "__main__":
    unittest.main()
