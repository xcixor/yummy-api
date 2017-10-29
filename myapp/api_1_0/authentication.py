"""Defines the api's routes for registration"""

from . import api

from flask import request, jsonify, make_response

from ..models import User

from ..models import User

import json


@api.route('/auth/register',  methods=['POST'])
def register():
    """Registers new users"""
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        confirm_password = request.json.get('confirm_password')

        if username and password and confirm_password:
            valid_username = User.validate_name(username)
            if not valid_username:
                response = {'message': 'Username cannot contain special characters except for underscores'}
                return make_response(jsonify(response)), 400
            if len(password)< 6:
                response = {'message': 'Username cannot be less than six characters'}
                return make_response(jsonify(response)), 400

            if password != confirm_password:
                response = {'message': 'Passwords do not match'}
                return make_response(jsonify(response)), 400

            reg_user = User.find_user(username)
            if not reg_user:
                user = User(username=username, password=password)
                user.save()
                response = {'message': 'Registered successfully'}
                return make_response(jsonify(response)), 201
            response = {'message': 'That user already exist'}
            return make_response(jsonify(response)), 202
        response = {'message': 'Please provide all required information'}
        return make_response(jsonify(response)), 400

@api.route('/auth/login',  methods=['POST'])
def login():
    """Validates the user's credentials and logs them in"""
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        if username and password:
            valid_username = User.validate_name(username)
            if valid_username:
                user = User.find_user(username)
                if user:
                    response = {'message': 'Login successful'}
                    return make_response(jsonify(response)), 200
                response = {'message': 'Username/Password combination is invalid, please check again'}
                return make_response(jsonify(response)), 401
            response = {'message': 'Username not valid'}
            return make_response(jsonify(response)), 400
        response = {'message': 'username/password not provided'}
        return make_response(jsonify(response)), 400
           
        
