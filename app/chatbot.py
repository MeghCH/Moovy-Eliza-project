import json
import os

import discord
from agent import basic_response, profile, recommendations, recommendations_per_genres
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from subfunctions.json_deleter import delete_json_file
from subfunctions.json_reader import read_json_file
from subfunctions.lookalike import lookalike

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Natural Language Processing setup
NLP_INTENTS = {
    "recommend": [
        "recommend",
        "reccomend",
        "recommand",
        "suggest",
        "advise",
        "suggestion",
    ],
    "movie": ["movie", "film", "movies", "films", "cinema"],
    "profile": ["profile", "data", "info", "information"],
    "delete": ["delete", "remove", "erase", "clear"],
    "help": ["help", "commands", "what can you do"],
    "policy": ["policy", "privacy", "data policy"],
    "json": ["json", "raw data", "profile data"],
    "lookalike": ["lookalike", "similar", "like", "same style"],
}


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


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_message = message.content.lower()
    discord_user = message.author.name

    words = set(user_message.split())

    if any(word in words for word in NLP_INTENTS["recommend"]) and any(
        word in words for word in NLP_INTENTS["movie"]
    ):
        try:
            thinking_message = await message.channel.send(
                f"{bot.user.name} is thinking..."
            )
            data = str(recommendations(discord_user))
            if thinking_message is not None:
                await thinking_message.delete()
            await message.channel.send(data)
        except Exception as e:
            await message.channel.send(f"An error occurred: {e}")

    # Read profile intent
    elif any(word in words for word in NLP_INTENTS["profile"]):
        data = read_json_file(discord_user)
        if data is None:
            await message.channel.send("Error: Could not read your profile JSON file.")
        else:
            await message.channel.send(
                f"Here is your profile data:\n```json\n{json.dumps(data, indent=4)}\n```"
            )

    # Delete intent
    elif any(word in words for word in NLP_INTENTS["delete"]) and any(
        word in words for word in NLP_INTENTS["profile"]
    ):
        delete_json_file(discord_user)
        await message.channel.send("Your data is fully deleted!")

    # Help intent
    elif any(word in words for word in NLP_INTENTS["help"]):
        await message.channel.send(
            "**Here are all the commands available:**\n\n"
            "`/help`: Shows all the commands available\n"
            "`/profile`: Generate a recommendation profile for each user based on the Letterboxd user.\n"
            "`/delete_profile`: Allows you to delete all the data about you.\n"
            "`/json`: Allows you to see the JSON recommendation profile.\n"
            "`/recommendation`: Recommend movies based on your profile.\n"
            "`/recommendation-genre`: Recommend movies based on a specific genre.\n"
            "`/lookalike`: Find 3 movies with a similar style to a movie you liked."
        )

    # Policy intent
    elif any(word in words for word in NLP_INTENTS["policy"]):
        policy_message = """
## **Privacy & Data Policy**
### **1. Data Collection:**
- The bot uses **publicly available data** from your Letterboxd profile (reviews, ratings, and watched movies).
- No private or sensitive data is collected.
### **2. Data Storage:**
- Your movie preferences are stored as a JSON file indefinitely.
- You can completely delete your profile anytime using `/delete_profile`.
### **3. Ethical Considerations:**
- **Transparency:** This bot is an AI tool, not a human. Recommendations are algorithmic.
- **No Filter Bubbles:** We include "hidden gems" to broaden your movie choices.
- **No Commercial Bias:** Recommendations are based on your tastes, not ads.
### **4. User Control:**
- Use `/delete_profile` to remove your data.
- Use `/profile` to start fresh.
### **5. Feedback & Improvements:**
- Your feedback helps improve the bot. Use `/feedback` to share your thoughts.
By using this bot, you agree to this policy. For questions, contact the developer.
"""
        await message.channel.send(policy_message)

    # Lookalike intent
    elif any(word in words for word in NLP_INTENTS["lookalike"]):
        try:
            thinking_message = await message.channel.send(
                f"{bot.user.name} is thinking..."
            )
            result = lookalike(user_message)
            if thinking_message is not None:
                await thinking_message.delete()
            await message.channel.send(result)
        except Exception as e:
            await message.channel.send(f"An error occurred: {e}")

    else:
        output = basic_response(user_message)
        await message.channel.send(output)

    await bot.process_commands(message)


# This below is the 'profile' function :
# It allow the bot to create a preference profile of the user based on his last Letterboxd Reviews

# Here are the command that uses / as a prefix. It uses the discrod embedded autocompletion system for a better visual and ux experience


@bot.tree.command(
    name="profile",
    description="Generate a user profile based on their Letterboxd Legged Reviews history",
)
@app_commands.describe(username="Username of your Letterboxd Account")
async def profile_slash_command(interaction: discord.Interaction, username: str):
    """Generate a user profile based on their Letterboxd history."""
    await interaction.response.send_message(
        f"*This bot uses your public Letterboxd reviews to generate recommendations. No private data is collected. By sending this command, you consent us to store public letterboxd data. See more here: `/policy`*\n**Generating profile for** {username}, **please wait a minute before sending another command**"
    )
    discord_user = interaction.user.name
    thinking_message = await interaction.followup.send(
        f"{bot.user.name} is generating your profile..."
    )
    profile(username, discord_user)
    if thinking_message is not None:
        await thinking_message.delete()
    await interaction.followup.send(
        f"Profile for {username} has been generated successfully!"
    )


# Here is the 'JSON' output function :
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


# Here is the Delete Profile function :
# It allows the user to delete his profile and stored data about him


@bot.tree.command(
    name="delete_profile",
    description="Allows the user to delete his profile from our data.",
)
async def delete_slash_profile(interaction: discord.Interaction):
    """Allows the user to delete his profile from our data."""
    discord_user = interaction.user.name
    delete_json_file(discord_user)
    await interaction.response.send_message(
        "Your data is fully deleted, see you at the next one !"
    )


# Here is the Help function :
# It allows the user to see all avaliables functions


@bot.tree.command(
    name="help",
    description="Shows all the commands avaliable.",
)
async def help_slash_profile(interaction: discord.Interaction):
    """Shows all the avaliable commands."""
    await interaction.response.send_message(
        "**There are all the commands avaliables :**\n\n`/help`: Shows all the commands avaliable\n`/profile`: Generate a recommandation profile for each user based on the Letterboxd user.\n`/delete_profile`: Allows you to delete all the data about you.\n`/json`: Allows you to see the json recommendation profile.\n`/reccomendation`: Reccomend you movies.\n`/reccomendation-genre`: Reccomend you movies depending of the genre.\n`/lookalike`: Reccomend you movies that looks like another movie"
    )


# Here is the Policy function :
# It allows the user to see the bot's policy


@bot.tree.command(
    name="policy",
    description="View the bot's privacy and data policy",
)
async def policy_command(interaction: discord.Interaction):
    policy_message = """
## **Privacy & Data Policy**
### **1. Data Collection:**
- The bot uses **publicly available data** from your Letterboxd profile (reviews, ratings, and watched movies).
- No private or sensitive data is collected.
### **2. Data Storage:**
- Your movie preferences are stored as a JSON file indefinitely.
- You can completely delete your profile anytime using `/delete_profile`.
### **3. Ethical Considerations:**
- **Transparency:** This bot is an AI tool, not a human. Recommendations are algorithmic.
- **No Filter Bubbles:** We include "hidden gems" to broaden your movie choices.
- **No Commercial Bias:** Recommendations are based on your tastes, not ads.
### **4. User Control:**
- Use `/delete_profile` to remove your data.
- Use `/profile` to start fresh.
### **5. Feedback & Improvements:**
- Your feedback helps improve the bot. Use `/feedback` to share your thoughts.
By using this bot, you agree to this policy. For questions, contact the developer.
"""
    await interaction.response.send_message(policy_message)


@bot.tree.command(
    name="recommendation",
    description="Recommend movies based on your profile.",
)
async def reco_slash_command(interaction: discord.Interaction):
    """Recommend movies based on his preference profile."""
    await interaction.response.defer()

    try:
        discord_user = interaction.user.name
        data = str(recommendations(discord_user))
        await interaction.followup.send(data)

    except Exception as e:
        await interaction.followup.send(f"Une erreur est survenue : {e}")


GENRES = [
    "Drama",
    "Family",
    "Fantasy",
    "Romance",
    "Comedy",
    "Animation",
    "Sci-Fi",
    "Action",
    "Adventure",
    "Documentary",
    "Horror",
    "History",
    "Musical",
    "Mystery",
    "Crime",
    "Sport",
    "Thriller",
    "War",
    "Western",
]


async def genre_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=genre, value=genre)
        for genre in GENRES
        if current.lower() in genre.lower()
    ][:25]


@bot.tree.command(
    name="recommendation-genre",
    description="Recommend movies based on a genre asked for.",
)
@app_commands.autocomplete(genre=genre_autocomplete)
async def reco_genre_slash_command(interaction: discord.Interaction, genre: str):
    """Recommend movies based on a specific genre asked for."""
    await interaction.response.defer()

    try:
        data = str(recommendations_per_genres(genre))
        await interaction.followup.send(
            f"There is a list of films for the genre **{genre}** :\n{data}"
        )

    except Exception as e:
        await interaction.followup.send(f"Une erreur est survenue : {e}")


@bot.tree.command(
    name="lookalike",
    description="Find 3 movies with a similar style to a movie you liked.",
)
@app_commands.describe(
    message="Describe the movie you want lookalikes for (e.g. 'I would like a film in the same style as Uncharted')"
)
async def lookalike_slash_command(interaction: discord.Interaction, message: str):
    """Find 3 movies similar in style to a given movie."""
    await interaction.response.defer()

    try:
        result = lookalike(message)
        await interaction.followup.send(result)
    except Exception as e:
        await interaction.followup.send(f"Une erreur est survenue : {e}")


@bot.tree.command(
    name="hello",
    description="Say hello to the user",
)
async def hello_slash_command(interaction: discord.Interaction):
    """Say hello to the user."""
    await interaction.response.send_message(
        f"Hello {interaction.user.mention}! How can I help you today?"
    )


load_dotenv()
token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
