import requests
from subfunctions.uniform_text import uniform_text

def get_movies_genres(genre): 
    genre = uniform_text(genre) 
    url = f"https://moviedb.wyliam.fr/genres/{genre}"
 
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else :
        return f"Error{response.status_code} : Genre not found."

def get_genre():
    url = f"https://moviedb.wyliam.fr/genres/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else : 
        return f"Error{response.status_code} : Not found"
    
get_movies_genres("drama")

    

    