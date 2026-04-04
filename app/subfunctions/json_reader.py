import json
import os


def read_json_file(user: str):
    """
    Read and return the content of a JSON file named USER.json.

    Args:
        user (str): The username for which to read the JSON file.

    Returns:
        dict: The JSON data as a dictionary, or None if an error occurs.
    """
    # Construct the file path
    file_path = f"cache/json/{user}.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    # Read and return the JSON file
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        return data

    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = input("Enter the username: ")

    data = read_json_file(user)
    if data is not None:
        print(json.dumps(data, indent=4))
