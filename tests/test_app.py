"""Test whether an instance of the app is created successfully and its context created"""

import sys

sys.path.append("..")

import unittest

from flask import current_app

from myapp import create_app


class BasicsTestCase(unittest.TestCase):
    """
    Inherits from testcase to create the test cases
    """
    def setUp(self):
        """Creates the objects used in the tests"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Cleans up the objects after the tests"""
        self.app_context.pop()

    def test_app_exists(self):
        """Tests if the app is created successfully"""
        self.assertFalse(current_app is None)
