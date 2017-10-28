"""Defines the api's routes for registration"""
import re

from . import api

from flask import request, jsonify, make_response

from ..models import User

from ..models import User

def validate_name(username):
    """Validates whether the username has special characters"""
    if re.match("^[a-zA-Z0-9 _]*$", username):
        return True
    return False


@api.route('/auth/register',  methods=['POST'])
def register():
    """Registers new users"""
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        confirm_password = request.json.get('confirm_password')

        if username and password and confirm_password:
            valid_username = validate_name(username)
            if not valid_username:
                response = {'message': 'Username cannot contain special characters except for underscores'}
                return make_response(jsonify(response)), 400
            if len(username)< 6:
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
                return make_response(jsonify(response)), 400
            response = {'message': 'That user already exist'}
            return make_response(jsonify(response)), 202
        response = {'message': 'Please provide all required information'}
        return make_response(jsonify(response)), 400

