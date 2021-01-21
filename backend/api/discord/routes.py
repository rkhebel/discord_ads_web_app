from flask import Blueprint, request, session, jsonify
from ..models import db, User, DiscordServer
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .. import jwt
from ..utils import json_required
from ..DiscordService import DiscordAPI

# Blueprint Configuration
discord = Blueprint(
    'discord', 
    __name__,
    url_prefix='/discord'
)

discord_service = DiscordAPI()

@discord.before_request
@jwt_required
def is_authorized():
  pass

@discord.route('/profile', methods=['GET'])
def profile():
  return jsonify({"msg": "This is not public yeet!"}), 200

@discord.route('/server', methods=['POST'])
@json_required(
  required_fields={'guild_id': 'Please provide an id for the server'},
  validations=[]
)
def create_server():
  guild_id = request.json.get('guild_id')
  guild = discord_service.guild(guild_id)
  current_user = get_jwt_identity()
  print(guild)

  server = DiscordServer(
    guild_id = guild_id,
    name = guild['name'],
    user_id = current_user,
    description = guild['description']
  )

  db.session.add(server)
  db.session.commit()
  
  return jsonify({'success': 'true'}), 200
