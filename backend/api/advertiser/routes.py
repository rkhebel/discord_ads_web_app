from flask import current_app as app
from flask import Blueprint, render_template, url_for, redirect, flash, request, session, jsonify
from ..models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .. import jwt

# Blueprint Configuration
advertiser = Blueprint(
    'advertiser', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/advertiser'
)

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        'ok': False,
        'message': 'Missing Authorization Header'
    }), 401


@advertiser.route('/', methods=['GET'])
@jwt_required
def dashboard():
  return jsonify({"msg": "This is not public yeet!"})
