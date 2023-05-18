import discord
import json
import os, sys
from components.objects import context
from components.commands import *

path = os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(path)

with open('config.json', "r") as f:
    config = json.load(f)

prefix = config["prefix"]

class myClient(discord.Client):
    async def on_ready(self):
        
        print(f"logged on as {self.user} (ID: {self.user.id}).")
        print(f"current prefix is : \"{prefix}\"")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content[0] != prefix:
            return

        array = message.content[1:].split(" ")
        cmd = array[0]
        args = array[1:]

        ctx = context(self,message, args)

        match(cmd):
            case "ping":
                await ping(ctx)

            case "av":
                await avatar(ctx)

            case "avatar":
                await avatar(ctx)
            
            case "sav":
                await serveravatar(ctx)
            
            case "serveravatar":
                await serveravatar(ctx)

            case "banner":
                await banner(ctx)

            case "whois":
                await whois(ctx)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = myClient(intents= intents)
client.run(config["token"])