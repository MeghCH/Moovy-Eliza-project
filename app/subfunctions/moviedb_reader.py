import os

import requests
from dotenv import load_dotenv
from subfunctions.uniform_text import uniform_text


def get_movies_genres(genre):
    load_dotenv()
    url = str(os.getenv("MOVIEDB_API")) + "/genres/" + str(uniform_text(genre))

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error{response.status_code} : Genre not found."


def get_genre():
    load_dotenv()
    url = str(os.getenv("MOVIEDB_API")) + "/genres/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error{response.status_code} : Not found"
