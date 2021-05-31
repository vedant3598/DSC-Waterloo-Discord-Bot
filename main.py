import discord
import os

PATH = ''
client = discord.Client()
# Add Discord Token here when bot is ready to be deployed
TOKEN = os.getenv(PATH)

@client.event
async def on_ready():
    print('{} is connected & ready to rumble!'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    

@client.event
async def on_member_join(member):
    channel = client.get_channel(837526205540073506)
    intro_channel = client.get_channel(848759566635499570)
    # Figure out how to link other channels in message
    await channel.send(
        "Hello {}! Welcome to the Google Developer Student Clubs, University of Waterloo chapter discord server." +
        "Please read our rules at the top of this channel".format(member.name)
    )
    await channel.send(
        "Say hi and introduce yourself in the introduction channel #" + intro_channel + "!"
    )

client.run()