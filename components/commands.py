from components.objects import context
import discord

async def ping(ctx: context):
    await ctx.channel.send("pong!")

async def avatar(ctx: context):
    if ctx.args:
        try:
            target = ctx.message.mentions[0]
        except IndexError:
            target = await ctx.client.fetch_user(int(ctx.args[0]))
    else:
        target = ctx.message.author

    if target.avatar is None:
        await ctx.channel.send("User has no avatar!")
        return

    embed = discord.Embed(color=0x581ca0, title=f"{target}\'s avatar")
    embed.set_image(url=target.avatar.url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)
    
    await ctx.channel.send(embed=embed)

async def serveravatar(ctx: context):
    if ctx.args:
        try:
            target = ctx.message.mentions[0]
        except IndexError:
            target = await ctx.client.fetch_user(int(ctx.args[0]))
    else:
        target = ctx.message.author

    if target.avatar is None:
        await ctx.channel.send("User has no avatar!")
        return
    
    embed = discord.Embed(color=0x581ca0, title=f"{target}\'s server avatar")
    embed.set_image(url=target.display_avatar.url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)
    
    await ctx.channel.send(embed=embed)

async def banner(ctx: context):
    if ctx.args:
        try:
            target = await ctx.client.fetch_user(ctx.message.mentions[0].id)
        except IndexError:
            target = await ctx.client.fetch_user(int(ctx.args[0]))
    else:
        target = await ctx.client.fetch_user(ctx.message.author.id)

    if target.banner is None:
        await ctx.channel.send("User has no banner!")
        return

    embed = discord.Embed(color=0x581ca0, title=f"{target}\'s banner")
    embed.set_image(url=target.banner.url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)
    
    await ctx.channel.send(embed=embed)

async def whois(ctx: context):
    if ctx.args:
        try:
            target = await ctx.client.fetch_user(ctx.message.mentions[0].id)
        except IndexError:
            target = await ctx.client.fetch_user(int(ctx.args[0]))
    else:
        target = await ctx.client.fetch_user(ctx.message.author.id)

    if ctx.channel.type != discord.ChannelType.private and ctx.channel.type != discord.ChannelType.group:
        member = ctx.server.get_member(target.id)
    
    embed = discord.Embed(title=f"{target.name}'s profile", color=0x581ca0)
    embed.set_thumbnail(url=target.avatar.url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)

    if member:
        newlist = []
        embed.url = None
        embed.add_field(name="username:", value=f"{member.name}#{member.discriminator} / <@{member.id}>", inline=False)
        embed.add_field(name="status:", value=member.status, inline=False)
        embed.add_field(name="userid:", value=member.id, inline=False)
        embed.add_field(name="created at:", value=member.created_at.strftime("%d/%m/%Y, %H:%M:%S"), inline=False)
        embed.add_field(name="joined at:", value=member.joined_at.strftime("%d/%m/%Y, %H:%M:%S"), inline=False)
        for role in member.roles:
            newlist += [f"<@&{role.id}>"]
        
        embed.add_field(name="roles:", value=', '.join(newlist[1:]) , inline=False)

    await ctx.channel.send(embed=embed)