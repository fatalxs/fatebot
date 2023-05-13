import discord

class myClient(discord.Client):
    async def on_ready(self):
        print(f"logged on as {self.user}")

    async def on_message(self,msg):
        print(f"message received from {msg.author}")
        if msg.author != self.user: # not a bot message
            await msg.channel.send("hey")

intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents= intents)
with open("config.json") as f:
    token = f["token"]
    
client.run(token)