# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:13:29 2022

@author: Baldwin-Akin Varner
"""

import discord
from discord.ext import commands, tasks
import youtube_dl
from random import choice
import music
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

status = ['Listenin to sumn fye!', 'Busy', 'Schleep']

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
    change_status.start()
    print('The Bot is active!')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)} ms')

@tasks.loop(minutes=60)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))



client.run(token)
