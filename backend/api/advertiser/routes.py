from flask import Blueprint, render_template, url_for, redirect, flash, request, session, jsonify
from ..models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .. import jwt
from ..utils import json_required
import sys
from traceback import format_exception
from flask_jwt_extended.exceptions import (
    JWTDecodeError, NoAuthorizationError, InvalidHeaderError, WrongTokenError,
    RevokedTokenError, FreshTokenRequired, CSRFError, UserLoadError,
    UserClaimsVerificationError
)
from jwt import (
    ExpiredSignatureError, InvalidTokenError, InvalidAudienceError,
    InvalidIssuerError, DecodeError
)

JWT_EXCEPTIONS = (
  JWTDecodeError, 
  NoAuthorizationError, 
  InvalidHeaderError, 
  WrongTokenError,
  RevokedTokenError, 
  FreshTokenRequired, 
  CSRFError, 
  UserLoadError,
  UserClaimsVerificationError,
  ExpiredSignatureError, 
  InvalidTokenError, 
  InvalidAudienceError,
  InvalidIssuerError, 
  DecodeError
)

##################################
# MOST OF THIS IS NOT FUNCTIONAL REMOVE WHEN COMPLETE
###################################

# Blueprint Configuration
advertiser = Blueprint(
    'advertiser', 
    __name__,
    url_prefix='/advertiser'
)

@advertiser.before_request
@jwt_required
def is_authorized():
  pass

# #catch all for server errors
# #and jwt unauthorized errors
# @advertiser.errorhandler(Exception)
# def server_error(err):
#   if isinstance(err, JWT_EXCEPTIONS):
#     return jsonify({
#       'ok': False,
#       'message': 'Missing Authorization Header'
#     }), 401
#   #for logging
#   etype, value, tb = sys.exc_info()
#   error_info = ''.join(format_exception(etype, value, tb))
#   print(error_info)
#   return jsonify({
#     'error': 'Internal server error', 
#     'success': False
#   }), 500

@advertiser.route('/advertisements', methods=['GET'])
@jwt_required
def get_advertisements():
  return jsonify({'message':'hello'}), 200
  # advertisements = Advertisements.query.filter_by(user_id=current_user)
  # return jsonify(advertisements)

@advertiser.route('/advertisements', methods=['POST'])
@json_required (
  required_fields = {
    'name': 'Please provide a name',
    'description': 'Please provide a description',
    'content': 'Please provide content'
  },
  validations = []
)
def create_advertisement():
  return jsonify({'message':'posting'}), 200
  name = request.json.get('name')
  description = request.json.get('description')
  content = request.json.get('content')
  advertisement = Advertisement(name = name, content = content, description = description)
  return

@advertiser.route('/advertisements', methods=['PUT'])
@json_required (
  required_fields = {},
  validations = []
)
def update_advertisements():
  return

@advertiser.route('/advertisements', methods=['DELETE'])
@json_required (
  required_fields = {},
  validations = []
)
def delete_advertisements():
  return

