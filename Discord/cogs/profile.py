#import required.
import discord
from discord.ext import commands

#import profiler specific
import aiohttp
import json, os, re, time, asyncio
import urllib.request

class Profile(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('Online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def pfp(self, ctx):
        url = "https://graphql.anilist.co/"
        oauth = 'TOKEN HERE'
        start = int(1)
        stop = int(10)
        await ctx.send('------STARTING------')
        while start < stop:
            payload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    users(sort: ID_DESC) {\\n      id\\n      avatar{\\n        large\\n      }\\n      \\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(start) + "}}"
            headers = {
                'content-type': "application/json",
                'authorization': "Bearer" + oauth
             }
            session = aiohttp.ClientSession()
            response = session.request("POST", url, data=payload, headers=headers)
            response = response.json()
            await ctx.send(response)
            #response = response.get('data', {})#.get('Page', {}).get('users', {})

            

def setup(client):
    client.add_cog(Profile(client))