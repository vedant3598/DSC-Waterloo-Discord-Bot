import discord
import os
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
# Discord Token for DSC_bot
TOKEN = 'DISCORD_TOKEN'

DSC_bot = commands.Bot(command_prefix='/', intents=intents)

def help_commands():
    help_embed = discord.Embed(
        title = 'Commands List',
        description = "Commands DSC_bot accepts",
        colour = discord.Colour.blue()
    )

    fields = [("/google_dev", "Link to Google Developer Tools site", False),
            ("/google_internships", "Link to Google Internships site", False),
            ("/server_info", "Prints information about server", False)]

    for name, value, inline in fields:
        help_embed.add_field(name=name, value=value, inline=inline)

    return help_embed


@DSC_bot.event
async def on_ready():
    print('{} is connected & ready to rumble!'.format(DSC_bot.user.name))

# Google Developer tools
@DSC_bot.command(name='google_dev')
async def google_developers(ctx):
    google_dev = discord.Embed(
        title = 'Google Developers',
        description = "[https://developers.google.com/](https://developers.google.com/)",
        colour = discord.Colour.green()
    )
    await ctx.send(embed = google_dev)

# Google internships page
@DSC_bot.command(name='google_internships')
async def google_intern(ctx):
    google_internships = discord.Embed(
        title = 'Google Internships',
        description = "[https://careers.google.com/students/](https://careers.google.com/students/)",
        colour = discord.Colour.blue()
    )
    await ctx.send(embed = google_internships)

# help command
@DSC_bot.command(name='commands')
async def help_output(ctx):
    await ctx.send(embed = help_commands())

# returns information about the server
@DSC_bot.command(name='server_info')
async def server_info(ctx):
    server = discord.Embed(
        title = 'Server Info',
        colour = discord.Colour.orange()
    )
    
    statuses = [len(list(filter(lambda x: str(x.status) == "online", ctx.guild.members))),
                len(list(filter(lambda x: str(x.status) == "offline", ctx.guild.members))),
                len(list(filter(lambda x: str(x.status) == "dnd", ctx.guild.members))),
                len(list(filter(lambda x: str(x.status) == "idle", ctx.guild.members)))]

    fields = [("ID", ctx.guild.id, True),
            ("Owner", ctx.guild.owner, True),
            ("Members", len(ctx.guild.members), True),
            ("Humans", len(list(filter(lambda x: not x.bot, ctx.guild.members))), True),
            ("Bots", (len(list(filter(lambda x: x.bot, ctx.guild.members)))), True),
            ("Text Channels", len(ctx.guild.text_channels), True),
            ("Voice Channels", len(ctx.guild.voice_channels), True),
            ("Statuses", f"🟢{statuses[0]} 😴{statuses[1]}  🔴{statuses[2]}  🌙{statuses[3]}", True),
            ("Command Prefix", "\\", True)
    ]    

    for name, value, inline in fields:
        server.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed = server)

# incorrect command points user to all possible commands the bot accepts
@DSC_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed = help_commands())


@DSC_bot.event
async def on_member_join(member):
    channel_introduction_id = discord.utils.get(member.guild.channels, name='introduction')
    welcome_rules_introduction_id = discord.utils.get(member.guild.channels, name='welcome-and-rules')

    channel_introduction = DSC_bot.get_channel(channel_introduction_id)
    welcome_rules_channel = DSC_bot.get_channel(welcome_rules_introduction_id)
    await channel_introduction.send(
        f"Hello {member.name}! Welcome to the Google Developer Student Clubs, University of Waterloo chapter discord server." +
        "Please read our rules at the top of this channel"
    )
    await channel_introduction.send(
        "Say hi and introduce yourself in the introduction channel #" + welcome_rules_channel + "!"
    )

DSC_bot.run(TOKEN)
