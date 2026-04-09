from subfunctions.json_reader import read_json_file


def get_pref_genre(user):
    json_user = read_json_file(user)

    if not json_user or not isinstance(json_user, dict):
        return "drama"

    try:
        profile = json_user.get("profile")
        if profile is not None:
            preffered = profile.get("top_genres", [])
        else:
            preffered = []

    except (KeyError, IndexError, TypeError) as e:
        print(f"Error: {e}")
        preffered = "drama"

    return preffered if preffered else "drama"
