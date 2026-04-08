from subfunctions.json_reader import read_json_file
import json

def get_pref_genre(user):
    json_user = read_json_file(user)
    
    if not json_user or not isinstance(json_user, dict):
        return 'drama'

    try:
        profile = json_user.get("profile")
        preffered = profile["top_genres"]
            
    except (KeyError, IndexError, TypeError):
        print("Error, not a drama this time")
        
    return preffered