#########################################
import requests

token = "" # Me [token] | Bot [token]
member = "" # Member ID
guild = "" # Guild ID
channel = "" # VoiceChannel ID
url = f"https://discord.com/api/v9/guilds/{guild}/members/{member}"
json = {'channel_id': channel}
head = {"authorization": token}
req = requests.patch(url, headers=head, json=json)
print(req.text) # Code By: Catcher#9802

#########################################
