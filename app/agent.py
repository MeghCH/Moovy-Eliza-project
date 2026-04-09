import json
import os

from dotenv import load_dotenv
from strands import Agent
from strands.models.ollama import OllamaModel
from subfunctions.profile_prompter import run_profile_prompter
from subfunctions.moviedb_reader import get_movies_genres
from subfunctions.get_preffered import get_pref_genre

load_dotenv()
ollama_model = OllamaModel(
    host=str(os.getenv("OLLAMA_URL")),
    model_id="granite4:latest",
)

agent = Agent(model=ollama_model)


def profile(username, discord_user):

    try:
        markdown_content = run_profile_prompter(username)
    except Exception as e:
        print(f"Error generating markdown content: {e}")
        return

    try:
        response = agent(markdown_content)
        print("Agent response:")
        print(response)

        response_content = str(response)

        try:
            profile_json = json.loads(response_content)
            os.makedirs("cache/json", exist_ok=True)
            output_path = f"cache/json/{discord_user}.json"
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(profile_json, json_file, indent=4)
            print(f"\nProfile saved to {output_path}")

        except json.JSONDecodeError as e:
            print("Error: The agent's response is not valid JSON.")
            print(f"Error details: {e}")

            os.makedirs("cache/json", exist_ok=True)
            output_path = f"cache/json/{discord_user}.json"
            with open(output_path, "w", encoding="utf-8") as json_file:
                json_file.write(response_content)
            print(f"Raw response saved to {output_path}")

    except Exception as e:
        print(f"Error sending content to the agent: {e}")
        import traceback

        traceback.print_exc()
    
def recommendations(discord_user):
    movies = []
    genres_list = get_pref_genre(discord_user)
    print(genres_list)
    for genre in genres_list:
        movies.append(get_movies_genres(genre))
    response = agent(
        f"""
            Here is a list of movies: {movies}

Based on this list, select exactly 2 movies for each of the following genres: {genres_list}.

Write only the raw message following this specific structure:
1. Start strictly with: "Since I know you like this kind of movies, here are some of them I can recommend to you..."
2. Group the movies by genre.
3. Use bold for the genre names and bullet points for the movies.

Nothing more, nothing less. No conversational filler.
        """
    )
    return response


def recommendations_per_genres(genre_asked):
  
    movies_list = get_movies_genres(genre_asked)
    print(f"Films trouvés pour {genre_asked}: {movies_list}")
   
    response = agent (
        f"""
        Here is a list of movies in the {genre_asked} genre: {movies_list}

            Based on this list, select exactly 3 to 5 high-quality movies.

            Write only the raw message following this specific structure:
            1. Start strictly with: "Since you're looking for {genre_asked} movies, here are some recommendations for you..."
            2. Use a bulleted list for the movies.
            3. Include a very brief (one sentence) description of why each movie fits the genre.

            Nothing more, nothing less. No conversational filler. Only the raw message.
        """
    )
    return response