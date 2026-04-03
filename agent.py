import json
import os

from strands import Agent
from strands.models.ollama import OllamaModel

from subfunctions.profile_prompter import run_profile_prompter

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="granite4:3b",
)

agent = Agent(model=ollama_model)


def profile():
    username = input("Letterboxd Username :")
    markdown_content = run_profile_prompter(username)

    print("Sending markdown content to the agent...")
    print("Markdown content:")
    print(markdown_content)

    response = agent(markdown_content)

    print("\nAgent response received:")
    print("Response type:", type(response))
    print("Response content:", response)

    response_content = str(response)

    print("\nAttempting to parse JSON...")
    try:
        profile_json = json.loads(response_content)
        os.makedirs("cache/json", exist_ok=True)
        with open(f"cache/json/{username}.json", "w", encoding="utf-8") as json_file:
            json.dump(profile_json, json_file, indent=4)
        print(f"Profile saved to cache/json/{username}.json")
    except json.JSONDecodeError as e:
        print("Error: The agent's response is not valid JSON.")
        print("Error details:", e)
        print("Response content:", response_content)

        os.makedirs("cache/json", exist_ok=True)
        response_lines = response_content.split("\n")
        if len(response_lines) > 2:
            cleaned_response = "\n".join(response_lines[1:-1])
        else:
            cleaned_response = response_content

        with open(
            f"cache/json/{username}_response.json", "w", encoding="utf-8"
        ) as json_file:
            json_file.write(cleaned_response)
        print(f"Raw response saved to cache/json/{username}_response.json")


if __name__ == "__main__":
    profile()
