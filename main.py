# Imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive
import random
import asyncio
import datetime as dt
from cheese_storage import cheese
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents=discord.Intents.all()
client=commands.Bot(command_prefix='ch!', intents=intents)
prefix='ch!'
@client.event
async def on_ready():
  print(f"{client.user} is connected to the following guilds:")
  for guild in client.guilds:
    print(f"Name: {guild.name}, ID: {guild.id}")
@client.command(name="gen", help="Generates a random cheese")
async def gen(ctx):
  print(f"Gen command used by {ctx.author.display_name} in {ctx.author.guild.name}")
  cheeselist=random.choice(cheese)
  embed=discord.Embed(title="The cheese you have generated is:")
  embed.set_image(url=cheeselist)
  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  await ctx.send("Generation Successful!", embed=embed)
@client.command(name="ping", help="Pings bot to check whether it is active.")
async def ping(ctx):
  print(f"Ping command used by {ctx.author.display_name} in {ctx.author.guild.name}")
  await ctx.channel.send("Pong")
keep_alive()
if __name__ == "__main__":
  client.run(TOKEN)