import discord
import os
import requests
import json


client = discord.Client()

def get_token():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  filepath = dir_path + '\\token'
  with open(filepath, 'r') as reader:
      tokenstr = reader.readline()
      json_token = json.loads(tokenstr)
      tokenId = json_token["TOKEN"]
      return tokenId

def get_joke():
    response = requests.get("https://api.yomomma.info")
    json_data = json.loads(response.text)
    joke = json_data["joke"] 
    return (joke)


def get_quote():
    response = requests.get("https://api.quotable.io/random")
    json_data = json.loads(response.text)
    quote = json_data["content"] + " -" + json_data["author"]
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$yo mama'):
        joke = get_joke()
        await message.channel.send(joke)

    if message.content.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)


client.run(get_token())
