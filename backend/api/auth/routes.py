from flask import Blueprint, render_template, url_for, redirect, flash, request, session, jsonify
from ..models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt, create_refresh_token, jwt_refresh_token_required
from .. import jwt
from ..utils import json_required
import re
from flask_jwt_extended.exceptions import (
    JWTDecodeError, NoAuthorizationError, InvalidHeaderError, WrongTokenError,
    RevokedTokenError, FreshTokenRequired, CSRFError, UserLoadError,
    UserClaimsVerificationError
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
  UserClaimsVerificationError
)

#types of users we can add to our db
USER_TYPES = ['advertiser', 'discord']

#used for validation
EMAIL_REGEX = re.compile(r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?")\

#this is how we invalidate jwt tokens
#note that on reset, we lost track of all invalid tokens. not that important since
#they only have a life of ~15minutes anyway, but something to keep in mind
#might want to implement table in db when doing refresh tokens
blacklist = set()

# Blueprint Configuration
auth = Blueprint(
    'auth', 
    __name__,
    url_prefix='/auth'
)

#catch all for server errors
#and jwt unauthorized errors
# @auth.errorhandler(Exception)
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

@auth.route('/login', methods=['POST'])
@json_required(
  required_fields = {
    'email': 'Please provide email',
    'password': 'Please provide password',
    'user_type': 'Please provide user type'
  },
  validations = [
    ('email', 'Please provide a valid email', lambda email: EMAIL_REGEX.match(email)),
    ('user_type', 'Please provide a valid user type', lambda user_type: user_type in USER_TYPES)
  ]
)
def login():
  email = request.json.get('email', None)
  password = request.json.get('password', None)
  user_type = request.json.get('user_type', None)

  user = User.query.filter_by(email=email, user_type=user_type).first()

  if not user:
    return jsonify({'error': 'No user associated with that email.'}), 400

  authorized = user.check_password(password)

  if not authorized:
    return jsonify({'error': 'Incorrect password!'}), 400

  access_token = create_access_token(identity=user.id)
  refresh_token = create_refresh_token(identity=user.id)
  user_type = user.user_type
  return jsonify(access_token=access_token, refresh_token=refresh_token, user_type=user_type), 200


@auth.route('/signup', methods=['POST'])
@json_required(
  required_fields = {
    'first_name': 'Please provide first name',
    'last_name': 'Please provide last name',
    'email': 'Please provide email',
    'password': 'Please provide password',
    'user_type': 'Please provide user type'
  },
  validations = [
    ('user_type', 'Please provide a valid user type', lambda user_type: user_type in USER_TYPES)
  ]
)
def signup():  
  first_name = request.json.get('first_name', None)
  last_name = request.json.get('last_name', None)
  email = request.json.get('email', None)
  password = request.json.get('password', None)
  user_type = request.json.get('user_type', None)

  user = User.query.filter_by(email=email, user_type=user_type).first()

  if user:
    return jsonify({'error': 'User with that email already exists.'}), 400

  user = User(
    first_name = first_name,
    last_name = last_name,
    email = email,
    user_type = user_type
  )
  user.set_password(password)
  db.session.add(user)
  db.session.commit()

  return jsonify({'success': 'true'}), 200

#checks if jwt is in blacklist before access
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
  jti = decrypted_token['jti']
  return jti in blacklist

@auth.route('/logout', methods=['POST'])
@jwt_required
def logout():
  jti = get_raw_jwt()['jti']
  blacklist.add(jti)
  return jsonify({'success': 'true'}), 200

#route to refresh access token
@auth.route('/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
  current_user = get_jwt_identity()
  access_token = create_access_token(identity=current_user)
  return jsonify(access_token=access_token), 200