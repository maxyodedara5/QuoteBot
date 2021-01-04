import discord
import os
import requests
import json

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def get_token():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  filepath = dir_path + '\\token'
  with open(filepath, 'r') as reader:
      tokenstr = reader.readline()
      json_token = json.loads(tokenstr)
      tokenId = json_token["TOKEN"]
      return tokenId

istokenbeing = get_token()
print(istokenbeing)

