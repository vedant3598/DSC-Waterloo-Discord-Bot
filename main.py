import discord
import os

client = discord.Client()
# Add Discord Token here when bot is ready to be deployed
TOKEN = os.getenv('')

@client.event
async def on_ready():
    print('{} is connected & ready to rumble!'.format(client.user))

@client.event
async def on_message(message):
    print()

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        
    )



client.run()