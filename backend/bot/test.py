from DiscordService import DiscordAPI
import utils

api = DiscordAPI()
guild_id = '753769674549886976'
guild = api.guild(guild_id)
system_channel_id = utils.get_default_channel(guild)
channels = api.guild_channels(guild_id)
message = {
  'content': 'hello'
}


response = api.create_message(system_channel_id, message)


print(response)