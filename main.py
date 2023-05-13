import discord
import json
import time

with open('config.json', "r") as f:
    config = json.load(f)

prefix = config["prefix"]


class myClient(discord.Client):
    async def on_ready(self):
        
        print(f"logged on as {self.user} (ID: {self.user.id}).")
        print(f"current prefix is : \"{prefix}\"")

    async def on_message(self,msg):
        if msg.content[0] != prefix:
            return

        array = msg.content[1:].split(" ")
        cmd = array[0]
        args = array[1:]

        if cmd == "ping":
            await msg.channel.send(f"pong!")

intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents= intents)

    
client.run(config["token"])