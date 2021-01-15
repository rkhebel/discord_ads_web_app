from flask import Blueprint, request, session, jsonify
from ..models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .. import jwt
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

# Blueprint Configuration
discord = Blueprint(
    'discord', 
    __name__,
    url_prefix='/discord'
)

@discord.before_request
@jwt_required
def is_authorized():
  pass

@discord.route('/', methods=['GET'])
def dashboard():
  return jsonify({"msg": "This is not public yeet!"})

@discord.route('/profile', methods=['GET'])
def profile():
  return jsonify({"msg": "This is not public yeet!"}), 200

