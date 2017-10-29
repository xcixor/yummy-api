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
            'password': 'pass',
            'confirm_password': 'pass'
        }
        self.user4 = {
            'username': 'mrndungu',
            'password': 'passone',
            'confirm_password': 'passtwo'
        }
        self.user5 = {
            'username': 'mrpeterndungu',
            'password': 'pass1',
            'confirm_password': 'pass1'
        }
        self.headers = {'Content-type': 'application/json'}
        self.url = '/auth/register'

    def tearDown(self):
        """Remove the created variables"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_username_validity(self):
        """Tests whether the username provided contains any special chatacters except underscores"""
        result = self.client().post(self.url, data=self.user1, headers=self.headers)
        self.assertEqual(result.status_code, 400)

    def test_password_length(self):
        result = self.client().post(self.url, data=self.user3, headers=self.headers)
        self.assertAlmostEqual(result.status_code, 400)

    def test_password_equal_confirmpassword(self):
        """Tests whether the confirmation password supplied matches the actual password"""
        result = self.client().post(self.url, data=self.user4, headers=self.headers)
        self.assertEqual(result.status_code, 400)

    def test_user_already_exists(self):
        """Tests whether registering user already exists"""
        self.client().post(self.url, data=self.user1, headers=self.headers)
        result = self.client().post(self.url, data=self.user1, headers=self.headers)
        self.assertEqual(result.status_code, 400)

    def test_register_user(self):
        """Tests whether a user can be registered successfully"""
        result = self.client().post(self.url, data=self.user5, headers=self.headers)
        self.assertEqual(result.status_code, 201)
        

        
