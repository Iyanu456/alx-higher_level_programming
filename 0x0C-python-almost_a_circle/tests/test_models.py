#!.usr/bin/python3
import unittest
import sys
from io import StringIO
import pep8
from models.base import base
import os
"""
This module contains all unittest for base class

"""

class TestBase(unittest.TestCase):
    """
    Class of function to run tests

    """
    def setup(self):
        """
        function to redirect stdout

        """
        sys.stdout = StringIo()

    def tearDown(self):
        """
        Cleans everything

        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Test for pep8  model

        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

     def test_pep8_test(self):
        """
        Test for pep8  test

        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_id(self):
        """
        Test check for id in Base class.

        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = baase()
        self.assertEqual(b1.id, 1)
	self.assertEqual(b2.id, 2)
	self.assertEqual(b3.id, 3)
	self.assertEqual(b4.id, 12)
	self.assertEqual(b5.id, 4)
