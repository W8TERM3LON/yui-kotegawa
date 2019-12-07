import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

#load Discord token from .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '~')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def clear(ctx, remove=10):
    await ctx.channel.purge(limit=remove)


cogs = "/home/david/Desktop/yui-kotegawa/Discord/cogs"
for filename in os.listdir( cogs ):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)