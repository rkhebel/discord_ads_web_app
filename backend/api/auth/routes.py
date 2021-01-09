from flask import current_app as app
from flask import Blueprint, render_template, url_for, redirect, flash, request, session, jsonify
from ..models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_types = ['advertiser', 'discord']

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
  return jsonify(access_token=access_token), 200


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
