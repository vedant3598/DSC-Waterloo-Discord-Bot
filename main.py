import discord
import os
from discord.ext import commands

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
# Discord Token for DSC_bot
TOKEN = 'ODQ4MzQyMTI2NDY2Njk1MjI4.YLLOLA.-n1I9cbuPGuNumfUhhkSINhMFLY'

DSC_bot = commands.Bot(command_prefix='/', intents=intents)

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
    server = discord.Embed(
        title = 'Server Info',
        colour = discord.Colour.orange()
    )
    
    # Will add guild information
    fields = [("ID", ctx.guild.id, True),
            ("Owner", ctx.guild.owner, True),
            ("Members", len(ctx.guild.members), True),
            ("Humans", (), True),
            ("Bots", (), True),
            ("Text Channels", len(ctx.guild.text_channels), True),
            ("Voice Channels", len(ctx.guild.voice_channels), True),
            ("Statuses")
    ]    

    for name, value, inline in fields:
        server.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed = server)

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