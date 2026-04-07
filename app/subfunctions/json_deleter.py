import os


def delete_json_file(user: str):
    file_path = f"cache/json/{user}.json"
    os.remove(file_path)
