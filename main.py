# Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive
import glob, random, asyncio, os
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents=discord.Intents.all()
client=commands.Bot(command_prefix='ch!', intents=intents)
prefix='ch!'
file_path_type = "./cheeses/*.jpg"
images = glob.glob(file_path_type)

@client.event
async def on_ready():
  print(f"{client.user} is connected to the following guilds:")
  for guild in client.guilds:
    print(f"Name: {guild.name}, ID: {guild.id}")
@client.command(name="gen", help="Generates a random cheese")
async def gen(ctx):
  async with ctx.typing():
    print(f"Gen command used by {ctx.author.display_name} in {ctx.author.guild.name}")
    embed=discord.Embed(title="The cheese you have generated is:")
    file = discord.File(f"{random.choice(images)}", filename="image.png")
    embed.set_image(url="attachment://image.png")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Source: Misc Wikipedia and Google Images")
    await asyncio.sleep(3)
  await ctx.send("Generation Successful!", file=file, embed=embed)
@client.command(name="ping", help="Pings bot to check whether it is active.")
async def ping(ctx):
  print(f"Ping command used by {ctx.author.display_name} in {ctx.author.guild.name}")
  await ctx.channel.send("Pong")
keep_alive()
if __name__ == "__main__":
  client.run(TOKEN)