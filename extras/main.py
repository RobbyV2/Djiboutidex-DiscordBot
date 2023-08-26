import json
import random
import time
import os
import math

import discord
from discord import *
from discord.ext import commands, tasks
from discord.ext.commands import bot
from discord.utils import get
from discord import app_commands

file = "config.json"

def getsetting(name):
    with open(file, 'r') as data:
        output = json.load(data)
    result = output[name]
    return result

prefix = getsetting("prefix")
application_id = getsetting("application_id")
token = getsetting("token")
status = getsetting("status")

intents = discord.Intents.messages()

bot = commands.Bot(command_prefix=prefix,
                   intents=intents,
                   case_insensitive=True,
                   reconnect=True,
                   application_id=application_id)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"""Logged in as {bot.user.name}!
ID: {bot.user.id}
Application ID: {application_id}
Prefix: {prefix}
Status: {status}""")
    await bot.change_presence(activity=discord.Activity(
	 type=discord.ActivityType.playing, name=status))

# TODO: Add command to automate generation of pfps.

bot.run(token)
