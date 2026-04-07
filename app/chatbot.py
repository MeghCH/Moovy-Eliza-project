import json
import os

import discord
from agent import profile
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from subfunctions.json_reader import read_json_file

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


# Theses are events :
# Some actions that runs in case of 'something' (connection, disconnection ...)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.event
async def on_connect():
    print("Bot connected!")


@bot.event
async def on_disconnect():
    print("Bot disconnected!")


@bot.event
async def on_resumed():
    print("Bot session resumed!")


# This below is the 'profile' function :
# It allow the bot to create a preference profile of the user based on his last Letterboxd Reviews


@bot.tree.command(
    name="profile",
    description="Generate a user profile based on their Letterboxd Legged Reviews history",
)
@app_commands.describe(username="Username of your Letterboxd Account")
async def profile_slash_command(interaction: discord.Interaction, username: str):
    """Generate a user profile based on their Letterboxd history."""
    await interaction.response.send_message(
        f"*This bot uses your public Letterboxd reviews to generate recommendations. No private data is collected. By sending this command, you consent us to store public letterboxd data.*\n**Generating profile for** {username}, **please wait a minute before sending another command**"
    )
    discord_user = interaction.user.name
    profile(username, discord_user)


# Here is the 'JSON' output' function :
# It's just a draft for the recommendation function : getting the JSON depending on the discord user


@bot.tree.command(
    name="json",
    description="Allows user to get the JSON profile file, only a draft for future features.",
)
async def json_slash_command(interaction: discord.Interaction):
    """Output the JSON depending on the discord user."""
    discord_user = interaction.user.name
    data = read_json_file(discord_user)

    if data is None:
        await interaction.response.send_message(
            "Error: Could not read your profile JSON file."
        )
        return

    await interaction.response.send_message(
        f"Here is your profile data:\n```json\n{json.dumps(data, indent=4)}\n```"
    )


load_dotenv()
token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
