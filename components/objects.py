import discord

class context():
    def __init__(self, client, message : discord.Message, args):
        self.client = client
        self.message = message
        self.channel = self.message.channel
        self.server = self.message.guild
        self.args = args