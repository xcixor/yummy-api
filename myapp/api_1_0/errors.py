""" Handles errors of the api"""

from flask import jsonify

from . import api

@api.errorhandler(404)
def error_404(error):
    """Triggered by 404 errors"""
    message = {
        'status': 404,
        'message': 'Sorry the resource was not found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

@api.errorhandler(500)
def error_500(error):
    """Triggered by 500 errors"""
    message = {
        'status': 500,
        'message': 'An unexpected error occured please try again later'
    }
    response = jsonify(message)
    response.status_code = 500
    return response

def bad_request(message):
    """Caused by invalid requests"""
    response = jsonify({'error': 'That request is invalid', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    """Triggered by a request that doesn't have authentication information"""
    response = jsonify({'error': 'That request is not authorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    """Triggered when authentication information provided with the request are not sufficient"""
    response = jsonify({'error': 'That request is not allowed', 'message': message})
    response.status_code = 403
    return response
