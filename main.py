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

    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        if message.content[0] != prefix:
            return

        ch = message.channel
        svr = message.guild

        array = message.content[1:].split(" ")
        cmd = array[0]
        args = array[1:]

        if cmd == "ping":
            await ch.send(f"pong!")
        
        if cmd == "av" or cmd == "avatar":
            if args:
                try:
                    target = message.mentions[0]
                except IndexError:
                    target = await self.fetch_user(int(args[0]))
            else:
                target = message.author

            embed = discord.Embed(color=0x581ca0, title=f"{target}\'s avatar")
            embed.set_image(url=target.avatar.url)
            embed.set_author(name=message.author, icon_url=message.author.avatar.url)
            
            await ch.send(embed=embed)
        
        if cmd == "banner":
            if args:
                try:
                    target = await self.fetch_user(message.mentions[0].id)
                except IndexError:
                    target = await self.fetch_user(int(args[0]))
            else:
                target = await self.fetch_user(message.author.id)

            if target.banner is None:
                await ch.send("User has no banner!")
                return

            embed = discord.Embed(color=0x581ca0, title=f"{target}\'s banner")
            embed.set_image(url=target.banner.url)
            embed.set_author(name=message.author, icon_url=message.author.avatar.url)
            
            await ch.send(embed=embed)


intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents= intents)

    
client.run(config["token"])