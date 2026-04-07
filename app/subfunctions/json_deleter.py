import os


def delete_json_file(user: str) -> None:
    json_path = f"cache/json/{user}.json"
    md_path = f"cache/prompt/{user}.md"

    for path in [json_path, md_path]:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError as e:
            print(f"Error deleting {path}: {e}")
