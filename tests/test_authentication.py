import sys

sys.path.append("..")

import unittest

from flask import current_app, jsonify

from myapp import create_app, db

import json


class UserTestCase(unittest.TestCase):
    """
    Test for user operations
    """

    def setUp(self):
        """Set up testing environment variables"""
        self.app = create_app('testing')
        self.client = self.app.test_client
        #bind app to current context
        self.app_context = self.app.app_context()
        self.app_context.push()
        #create database tables
        db.create_all()
        self.client = self.app.test_client
        self.user1 = {
            'username': 'mrpeter',
            'password': 'pass1',
            'confirm_password': 'pass1'
        }
        self.user2 = {
            'username': 'mr##ndungu',
            'password': 'password',
            'confirm_password': 'password'
        }
        self.user3 = {
            'username': 'mrndungu',
            'password': 'password',
            'confirm_password': 'passwordtwo'
        }

    def tearDown(self):
        """Remove the created variables"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_username_validity(self):
        """Tests whether the username provided contains any special chatacters except underscores"""
        result = self.client().post('/auth/register',
                                 data={'username': 'ndu#4%@#$', 'password': 'somepassword', 'confirm_password': 'somepassword'})


        # result = self.client().post('/auth/register', data=jsonify(self.user2))
        self.assertEqual(result.status_code, 400)