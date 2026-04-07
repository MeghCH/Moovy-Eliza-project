import requests
def get_movies_genres(genre): 

    url = f"http://localhost:8600/genres/{genre}"
 
    response = requests.get(url)

    print (response.json())
    
    if response.status_code == 200:
        data = response.json()
        return data
    else :
        return f"Error{response.status_code} : Genre not found."

def get_genre():
    url = f"http://localhost:8600/genres/"

    response = requests.get(url)
    print (response.json())

    if response.status_code == 200:
        data = response.json()
        return data
    else : 
        return f"Error{response.status_code} : Not found"
    
get_movies_genres("drama")
