import os

from strands import Agent
from strands.models.ollama import OllamaModel
from dotenv import load_dotenv
from subfunctions.moviedb_reader import get_genre, get_movies_genres

load_dotenv()

_ollama_model = OllamaModel(
    host=str(os.getenv("OLLAMA_URL")),
    model_id="granite4:latest",
)

_agent = Agent(model=_ollama_model)


def lookalike(user_message: str) -> str:
    all_genres = get_genre()

    movies_by_genre = {}
    if isinstance(all_genres, list):
        for genre in all_genres:
            genre_name = genre if isinstance(genre, str) else genre.get("name", "")
            if genre_name:
                result = get_movies_genres(genre_name)
                if isinstance(result, list):
                    movies_by_genre[genre_name] = result

    response = _agent(
        f"""
        The user wrote: "{user_message}"

        Extract the movie title the user is referring to from that message.
        Then, from the list of movies below, pick exactly 3 movies that are similar in style, tone, or genre to that movie.

        Write only the recommendation message addressed to the user.
        The message should follow this style:
        'Since you liked [movie title], here are 3 movies with a similar style you might enjoy: ...'
        Include the movie title and a short one-sentence reason for each pick.

        Available movies by genre:
        {movies_by_genre}
        """
    )
    return str(response)
