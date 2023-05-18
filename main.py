import discord
import json
import os, sys
from components.objects import context
from components import commands as cmds

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
                await cmds.ping(ctx)

            case "av":
                await cmds.avatar(ctx)

            case "avatar":
                await cmds.avatar(ctx)
            
            case "sav":
                await cmds.serveravatar(ctx)
            
            case "serveravatar":
                await cmds.serveravatar(ctx)

            case "banner":
                await cmds.banner(ctx)

            case "whois":
                await cmds.whois(ctx)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = myClient(intents= intents)
client.run(config["token"])