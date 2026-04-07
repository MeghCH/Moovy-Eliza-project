import os


def delete_json_file(user: str):
    json_path = f"cache/json/{user}.json"
    md_path = f"cache/prompt/{user}.md"
    try
        os.remove(json_path)
        os.remove(md_path)
    except
        pass
