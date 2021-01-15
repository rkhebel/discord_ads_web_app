# This file contains functions for interacting with the discord API

import discord #not using for now, too complicated with async stuff
import os
import requests
from dotenv import load_dotenv
load_dotenv()

BASE_URL = 'https://discord.com/api'
TOKEN = os.getenv('DISCORD_TOKEN')

class DiscordAPI():

  def __init__(self):
    self.base_url = BASE_URL
    self.session = requests.Session()
    self.session.headers['Authorization'] = 'Bot ' + TOKEN

  # USER ENDPOINTS

  def current_user(self):
    return self.session.get(self.base_url + '/users/@me').json()

  ## IMPORTANT NOTE ONLY RETURNS 100 GUILDS
  # this will only be useful for testing at start, probably shouldnt use going forward
  # since we cant get an exhaustive list of guilds
  def guilds(self):
    return self.session.get(self.base_url + '/users/@me/guilds').json()

  # GUILD ENDPOINTS

  def guild(self, guild_id):
    return self.session.get(self.base_url + f'/guilds/{guild_id}').json()

  def guild_channels(self, guild_id):
    return self.session.get(self.base_url + f'/guilds/{guild_id}/channels').json()
  
  def guild_members(self, guild_id):
    return self.session.get(self.base_url + f'/guilds/{guild_id}/members').json()

  # CHANNEL ENDPOINTS

  def channel(self, channel_id):
    return self.session.get(self.base_url + f'/channels/{channel_id}').json()

  def create_message(self, channel_id, message):
    return self.session.post(
      self.base_url + f'/channels/{channel_id}/messages',
      data = message
      ).json()

  

  

