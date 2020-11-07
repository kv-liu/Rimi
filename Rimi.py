#Rimi.py
import os

import discord
from dotenv import load_dotenv
import datetime
from discord.ext import commands, timers
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


bot = commands.Bot(command_prefix='!')

@bot.command(name="remind")
async def remind(ctx, time, *, reminder):
    date = datetime.datetime(*map(int, time.split("/"))) #Date must be in Y/M/D format

    timers.Timer(bot, "reminder", date, args=(ctx.channel.id, ctx.author.id, reminder)).start()

@bot.event
async def on_reminder(channel_id, author_id, reminder):
    channel = bot.get_channel(channel_id)
    
    await channel.send("Hey <@{0}>, remember to: {1}".format(author_id, reminder))

@bot.command(name="test")
async def test(ctx, arg):
    await ctx.send("Hey {0}, here is what you inputted: {1}".format(ctx.author.mention, arg))


bot.run("TOKEN")
