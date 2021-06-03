import discord
import os
from discord.ext import commands

client = discord.Client()
# Add Discord Token here when bot is ready to be deployed
TOKEN = 'ODQ4MzQyMTI2NDY2Njk1MjI4.YLLOLA.-n1I9cbuPGuNumfUhhkSINhMFLY'

DSC_bot = commands.Bot(command_prefix='/')

@DSC_bot.event
async def on_ready():
    print('{} is connected & ready to rumble!'.format(DSC_bot.user.name))

# Google Developer tools
@DSC_bot.command(name='Google')
async def gcp(ctx):
    google_dev = discord.Embed(
        title = 'Google Developers',
        description = "[https://developers.google.com/](https://developers.google.com/)",
        colour = discord.Colour.green()
    )
    await ctx.send(embed = google_dev)


# scrapes Google to find Google Internships - will do later
#@DSC_bot.command(name='Google Internships')
#async def gcp(ctx):
#    response = ""
#    await ctx.send(response)

# returns information about the server
@DSC_bot.command(name='server_info')
async def server_info(ctx):
    guild = DSC_bot.fetch_guild(837526205540073502)
    channels = await guild.fetch_channels()
    members = await guild.fetch_members().flatten()
    
    channels_message = discord.Embed(
        title = 'Channels',
        description = channels,
        colour = discord.Colour.orange()
    )

    members_message = discord.Embed(
        title = 'Members',
        description = members,
        colour = discord.Colour.orange()
    )

    await ctx.send(embed = channels_message)
    await ctx.send(embed = members_message)

@DSC_bot.event
async def on_member_join(member):
    channel = DSC_bot.get_channel(837526205540073506)
    intro_channel = DSC_bot.get_channel(848759566635499570)
    # Figure out how to link other channels in message
    await channel.send(
        "Hello {}! Welcome to the Google Developer Student Clubs, University of Waterloo chapter discord server." +
        "Please read our rules at the top of this channel".format(member.name)
    )
    await channel.send(
        "Say hi and introduce yourself in the introduction channel #" + intro_channel + "!"
    )

DSC_bot.run(TOKEN)