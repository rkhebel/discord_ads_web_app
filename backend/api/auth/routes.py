from flask import current_app as app
from flask import Blueprint, render_template, url_for, redirect, flash, request, session, jsonify
from ..models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt, create_refresh_token, jwt_refresh_token_required
from .. import jwt

#types of users we can add to our db
user_types = ['advertiser', 'discord']

#this is how we invalidate jwt tokens
#note that on reset, we lost track of all invalid tokens. not that important since
#they only have a life of ~15minutes anyway, but something to keep in mind
#might want to implement table in db when doing refresh tokens
blacklist = set()

# Blueprint Configuration
auth = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)

@auth.route('/login', methods=['POST'])
def login():
  if not request.is_json:
    return jsonify({'error': 'Missing JSON in request'}), 400

  email = request.json.get('email', None)
  password = request.json.get('password', None)
  user_type = request.json.get('user_type', None)

  if not email:
    return jsonify({'error': 'Missing email parameter'}), 400
  if not password:
    return jsonify({'error': 'Missing password parameter'}), 400
  if not user_type:
    return jsonify({'error': 'Missing user_type parameter'}), 400
  if user_type not in user_types:
    return jsonify({'error': 'Incorrect user type'}), 400

  user = User.query.filter_by(email=email, user_type=user_type).first()


  if not user:
    return jsonify({'error': 'No user associated with that email.'}), 400

  authorized = user.check_password(password)

  if not authorized:
    return jsonify({'error': 'Incorrect password!'}), 400

  access_token = create_access_token(identity=user.id)
  refresh_token = create_refresh_token(identity=user.id)
  return jsonify(access_token=access_token, refresh_token=refresh_token), 200


@auth.route('/signup', methods=['POST'])
def signup():
  if not request.is_json:
    return jsonify({'error': 'Missing JSON in request'}), 400
  
  first_name = request.json.get('first_name', None)
  last_name = request.json.get('last_name', None)
  email = request.json.get('email', None)
  password = request.json.get('password', None)
  user_type = request.json.get('user_type', None)

  if not first_name or not last_name or not email or not password or not user_type:
    return jsonify({'error': 'Missing parameter'}), 400

  if user_type not in user_types:
    return jsonify({'error': 'Incorrect user type'}), 400

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
@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
  current_user = get_jwt_identity()
  access_token = create_access_token(identity=current_user)
  return jsonify(access_token=access_token), 200