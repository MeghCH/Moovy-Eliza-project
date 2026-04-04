import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from agent import profile

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_connect():
    print("Bot connected!")


@bot.event
async def on_disconnect():
    print("Bot disconnected!")


@bot.event
async def on_resumed():
    print("Bot session resumed!")


@bot.command(name="profile")
async def generate_profile(ctx, username: str):
    """Generate a user profile based on their Letterboxd history."""
    await ctx.send(f"Generating profile for {username}")
    discord_user = ctx.author.name
    profile(username, discord_user)


load_dotenv()
token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
