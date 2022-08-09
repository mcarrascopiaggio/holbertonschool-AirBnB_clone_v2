#!/usrb/bin/python3
import sys
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import console
from models.engine.file_storage import FileStorage
import unittest

class test_console(unittest.TestCase):
    """Console Test"""
    
    def initilize(self):
        """Create the command instance"""
        self.instance = HBNBCommand()
        
    def test_documentation(self):
        """
        Test if there is documentation
        """
        self.assertTrue(len(console.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.__doc__) > 0)