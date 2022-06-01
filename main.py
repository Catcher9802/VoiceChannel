#########################################
import requests

token = "OTY3NTE0MTI1NTAyNjU2NTQ2.Yniepw.sx_FLmXgJgZ1YhJdL0HtZzPzXBg" # Me [token] | Bot [token]
member = "967514125502656546" # Member ID
guild = "975041492164935710" # Guild ID
channel = "980796957436051466" # VoiceChannel ID
url = f"https://discord.com/api/v9/guilds/{guild}/members/{member}"
json = {'channel_id': channel}
head = {"authorization": token}
req = requests.patch(url, headers=head, json=json)
print(req.text) # Code By: Catcher#9802

#########################################